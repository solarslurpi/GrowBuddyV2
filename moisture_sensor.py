from logging_handler import LoggingHandler
import paho.mqtt.client as mqtt

class MoistureSensor:
    def __init__(self):
        pass
    def _get_and_store_reading(self):
        """Subscribe to the mqtt message for moisture_sensor.  When a reading is received, store it
            into the growBuddy influxdb databaswe.
        """
        pass