import logging
from vpd_controller import VPDcontroller,growthStage

TYELLOW =  '\033[33m' # Yellow Text
TORIGINAL =  '\033[m' # reset to original (off-white)

def values_callback(time,temp,RH,vpd):
    """VPDcontroller calls vpd_buddy back sending the values from the mqtt message.  We'll store
    them nto an InfluxDB database.

    Args:
        time (datetime): Date and time of the reading.
        temp (float): Temperature in F
        RH (float): Relative Humidity
        vpd (float): Vaper Pressure Deficit
    """
    print(TYELLOW + f'Time is {time} Temperature is: {temp}℉   Relative Humidity is: {RH}% and vpd is: {vpd}'+TORIGINAL)
    # TODO: Store in influxdb



if __name__ == '__main__':
    # Once VPDController spins up mqtt, there is nothing to call.  values_callback is
    # called back to return readings. 
    VPDcontroller(growthStage.BABY, values_callback,logging.DEBUG)