# Welcome
I am passionate about optimizing grow room automation in my indoor home grow.  As the grows go by, I learn.  I think about what I can optimize.  My current obsession is optimizing VPD.  I am not building a generic solution because I don't need one.  My indoor grow:
- is in my kitchen in the same climate controlled environment I live in.  The temperature is typically around 70℉ and the humidity runs around 50%.  With the LEDs on, the grow tent environment is a few degrees higher.  Given an above day temperature of 70 ℉ or above, I will only adjust humidity.  Since the humidity is moderately low, I will use a humidifier but not a dehumidifier.
- is a bed of living soil.  Perhaps unusual to have a bed of soil in a kitchen, but I can't stop thinking about happy microbes.

Because the indoor climate control is close to ideal except for lower humidity, automating VPD to the ideal value will mean turning a DIY humidifier on and off.  I am using a DIY himidifier because I couldn't find one that was easy to automatically refill and didn't have the fitting I wanted.
# VPD Buddy System Overview
__VPD Buddy__ adjusts the humidity to ideal VPD ranges for the given growth stage the plants are in.

<img src="https://docs.google.com/drawings/d/e/2PACX-1vTjks0iZHIZyD4VEdOo01_se0jn_CgJu9JUCee-rUhXBmFfykmObBkpqSUFBkOvnIdisiIzygPvDeZa/pub?w=599&amp;h=332">

VPD Buddy includes:
## SnifferBuddy

[SnifferBuddy](https://github.com/solarslurpi/GrowBuddy/blob/main/pages/SNIFFER_BUDDY.md) takes CO2 level, temperature, and humidity readings.  I will use the same SnifferBuddy I used last time.  It sends an mqtt message `tele/snifferbuddy/SENSOR` handled by the `growbuddy` broker with the payload `{"Time":"2022-09-06T08:52:59","ANALOG":{"A0":542},"SCD30":{"CarbonDioxide":814,"eCO2":787,"Temperature":71.8,"Humidity":61.6,"DewPoint":57.9},"TempUnit":"F"}` every twenty seconds. 

 ![snifferbuddy mqtt](images/mqttexplorer_snifferbuddy.jpg)   
            [MQTT Explorer](http://mqtt-explorer.com/) showing snifferbuddy messages.
    
_Note: I've been using a scd30 (or scd40) because these sensors have awesome CO2 detection._

I let VPD Buddy know what stage the plants are at - baby, vegetative (veg), or flower.

_Note: I enter the growth stage - either Baby, Vegetative, or Flower._

The VPD Controller reads in the setpoint values for the VPD given the growth stage the plants are in. The source for the ideal VPD values is Pulse's [_The Ultimate Vapor Pressure Deficit (VPD) Guide_](https://pulsegrow.com/blogs/learn/vpd).  I take the average value of the range and use that as the setpoint value.

![Pulse VPD ranges](https://cdn.shopify.com/s/files/1/2451/2393/files/VPD_Stages_Card-Recovered_600x600.jpg)
# VPD Manager
- __VPD Manager__ for Managing the Amount of Water Vapor:
    - Subscribes to the SnifferBuddy (mqtt) messages to get the environment's temperature and humidity.
    - Uses a PID controller to return the number of seconds the humidifier should be turned on to get to the setpoint.  
    - Controller that adjusts the humidity to ideal VPD ranges for the given growth stage the plants are in.
    - humidifier that is plumbed to be autofilled and responds to on/off requests from the Controller.
# Actuator
The ___Actuator code__ turn on and off the humidifier.  _Note: This could be modified to actuate other devices, like a dehumidifier, heater, cooler, ..././

# Goals
- Collect data for historical use.  Not for adjustments.  The VPD is "set and forget".  If there is a problem, VPD 

# VPD Buddy




# Managing Irrigation
Another thing to dial in is irrigation.  My strategy is to use Blumats.  To dial in the opening/closing of the Blumat valve, the soil the Blumat system will irrigate needs to be at the ideal wetness.  To do that, I'll calibrate some wifi enabled soil moisture sensors