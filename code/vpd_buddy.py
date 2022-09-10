
from inspect import _void
import json
import math
import os
import logging

import paho.mqtt.client as mqtt
from logging_handler import LoggingHandler
from enum import Enum

settings_filename = 'vpd_settings.json'

class growthStage(Enum):
    BABY = 1
    VEG = 2
    FLOWER = 3

class VPDcontroller():
    '''Keep the Vaper Pressure Deficit at an ideal level'''
    def __init__(self, growth_stage = growthStage.BABY, get_values_callback=None,log_level=logging.DEBUG):
        # Used for initialization of PID controller when the first mqtt message from SnifferBuddy comes in.
        self.first_message = True
        self.get_values_callback = get_values_callback

        # Set up logging to go to the console.
        self.logger = LoggingHandler(log_level)
        self.logger.debug("-> Initializing VPDcontroller class")
        # Get settings out of JSON file.
        try:
            self.settings = self._read_settings()
            self.logger.debug(f'...Settings: {self.settings}')
        except Exception as e:
            self.logger.debug1(f'...Exiting due to Error: {e}')
            os._exit(1)

 
        # Set up the PID
        self.setpoint = 0.0
        if growth_stage == growthStage.BABY:
            self.setpoint = self.settings['baby_setpoint']
        elif growth_stage == growthStage.VEG:
            self.setpoint = self.settings['veg_setpoint']
        else:
            self.setpoint = self.settings['flower_setpoint']
        # The setpoint should be around .6 to 1.6...
        if not isinstance(self.setpoint,float) or self.setpoint*10 not in range(20):
            raise Exception ( "The vpd setpoint should be a floating point number between 0.0 and 2.0")
        self.logger.debug(f'The value for the vpd setpoint is: {self.setpoint}')
        self.pid_cum_error = 0.0
        self.pid_last_error = 0.0

        # Connect up with mqtt.
        try:
            client = mqtt.Client('vpdBuddy')
            client.on_message = self._on_message
            client.on_connect = self._on_connect
            client.connect(self.settings['mqtt_broker'])
            # At this point, mqtt drives the code.
            self.logger.debug('VPDcontroller has been initialized.  Handing over to mqtt.')
            client.loop_forever()


        except Exception as e:
            self.logger.debug1(f'...Exiting due to Error: {e}')
            os._exit(1)


    def _read_settings(self) -> dict:
        """Opens the JSON file identified in settings_file and reads in the settings as a dict.

        Raises:
            Exception: When it can't find the file named by the settings_filename attribute.  Most likely this file is named vpd_settings.json.

        Returns:
            dict: including values for the mqtt broker, topic, and vpd setpoints at the different 
            growth stages.
        """
        self.logger.debug(f'-> Reading in settings from {settings_filename} file.')
        dict_of_settings = {}
        try:
            with open(settings_filename) as json_file:
                dict_of_settings = json.load(json_file)
        except Exception as e:
            raise Exception(f'Could not open the settings file named {settings_filename}')
        return dict_of_settings

    def _on_connect(self,client, userdata, flags, rc) -> _void:
        '''Called back by the mqtt library once the code has connected with the broker.  Now we can subscribe to SensorBuddy readings.'''
        self.logger.debug(f"-> Mqtt connection returned {str(rc)}")
        mqtt_topic = self.settings['mqtt_topic']
        client.subscribe(mqtt_topic)
        self.logger.debug(f'subscribed to topic:{mqtt_topic}')


    def _on_message(self, client, userdata, msg) -> _void:
        """Received a reading from SnifferBuddy

        Args:
            userdata (_type_): _description_
            msg (_type_): _description_
        """
        message = msg.payload.decode(encoding='UTF-8')
        self.logger.debug(f'mqtt received message...{message}')
        vpd = self._calc_vpd(message)
                # Update the PID controller.
        pid_output = self._pid(self.setpoint,vpd)
        self.logger.debug(f'vpd: {vpd}   pid output: {pid_output}')



    
    def _calc_vpd(self,msg_str) -> float:
        """ Calculate the vpd based on the temp and humidity readings in the msg_str"""
        """ NOTE: The mqtt message has the scd model, in this case SCD30...this isn't generic.  ToDo: Generic"""
        dict = json.loads(msg_str)
        air_T = dict["SCD30"]["Temperature"]
        RH = dict["SCD30"]["Humidity"]
        if not isinstance(air_T,float) or not isinstance(RH,float) or air_T <= 0.0 or RH <= 0.0:
            raise Exception(f'Received unexpected values for either the temperature ({air_T}) or humidity ({RH}) or both')
         # While accuracy dictates using an IR thermometer to measure a leaf's temperature, the level of accuracy using 2 degrees less than air is "good enough".
        leaf_T = air_T -2
        vpd = 3.386*(math.exp(17.863-9621/(leaf_T+460))-((RH/100)*math.exp(17.863-9621/(air_T+460))))
        if self.get_values_callback:
            self.get_values_callback(air_T, RH, vpd)


        return(vpd)

    def _pid(self, setpoint, reading) -> int:
        Kp = self.settings['Kp']
        Ki = self.settings['Ki']
        Kd = self.settings['Kd']
        # This code is designed for my setup.  The indoors is climate cocntrolled.  There is only a humidifier to turn on or off - that is, it is always the case more humidity is needed and
        # the air temperature is a comfortable range for the plants.
        # If setpoint - reading is positive, the air in the grow room is too humid.  Most (pretty much all?) of the time the error should be negative.
        error = setpoint - reading
        if error > 0.0:
            return 0
        # Calculate the Proportional Correction
        pCorrection = Kp * error
        # Calculate the Integral Correction
        self.pid_cum_error += error
        iCorrection = Ki * self.pid_cum_error
        # Calculate the Derivitive Correction
        slope = error - self.pid_last_error
        dCorrection = Kd * slope
        self.pid_last_error = error
        # Calculate the # Seconds to turn Humidifier on.  I am roughly guessing 1 second on lowers VPD by .01.  A Wild Guess to be sure.
        nSecondsON = abs( int( (pCorrection + iCorrection + dCorrection)*100 ) )
        self.logger.debug(f'Number of seconds to turn on the Humdifier is {nSecondsON}.')
        return nSecondsON