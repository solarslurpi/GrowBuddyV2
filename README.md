# Welcome
I am passionate about optimizing grow room automation in my indoor home grow.  As the grows go by, I learn.  I think about what I can optimize.  My current obsession is optimizing VPD.  I am not building a generic solution because I don't need one.  My indoor grow:
- is in my kitchen in the same climate controlled environment I live in.
- is a bed of living soil.  Perhaps unusual to have a bed of soil in a kitchen, but I can't stop thinking about happy microbes.
- indoor humidity typically ranges from 40 to 50 percent.  The grow area tends to need more water vapor in the air, not less.
- indoor temperature typically ranges from 65 to 72 degrees F.  With the LEDs on, the grow tent environment is a few degrees higher.
because the indoor climate control is close to ideal except for lower humidity, automating VPD to the ideal value will mean turning a DIY humidifier on and off.  I am using a DIY himidifier because I couldn't find one that was easy to automatically refill and didn't have the fitting I wanted.
# VPD Buddy System Overview
__VPD Buddy__ adjusts the humidity to ideal VPD ranges for the given growth stage the plants are in.

<img src="https://docs.google.com/drawings/d/e/2PACX-1vTjks0iZHIZyD4VEdOo01_se0jn_CgJu9JUCee-rUhXBmFfykmObBkpqSUFBkOvnIdisiIzygPvDeZa/pub?w=599&amp;h=332">

VPD Buddy includes:


[SnifferBuddy](https://github.com/solarslurpi/GrowBuddy/blob/main/pages/SNIFFER_BUDDY.md) takes CO2 level, temperature, and humidity readings.  I will use the same SnifferBuddy I used last time.  It sends an mqtt message `tele/snifferbuddy/SENSOR` handled by the `growbuddy` broker with the payload `{"Time":"2022-09-06T08:52:59","ANALOG":{"A0":542},"SCD30":{"CarbonDioxide":814,"eCO2":787,"Temperature":71.8,"Humidity":61.6,"DewPoint":57.9},"TempUnit":"F"}` every twenty seconds. 

 ![snifferbuddy mqtt](images/mqttexplorer_snifferbuddy.jpg)   
            [MQTT Explorer](http://mqtt-explorer.com/) showing snifferbuddy messages.
    
_Note: I've been using a scd30 (or scd40) because these sensors have awesome CO2 detection._

I let VPD Buddy know what stage the plants are at - baby, vegetative (veg), or flower.

_Note: I enter the growth stage when the system starts up and when I decide it is not in vegetative as well as when I flip to flower.  This is the only input I need to make._

The VPD Controller reads in the range of ideal values for the VPD given the growth stage the plants are in. The source for the ideal VPD values is Pulse's [_The Ultimate Vapor Pressure Deficit (VPD) Guide_](https://pulsegrow.com/blogs/learn/vpd)

![Pulse VPD ranges](https://cdn.shopify.com/s/files/1/2451/2393/files/VPD_Stages_Card-Recovered_600x600.jpg)


- VPD Manager for Managing the Amount of Water Vapor:
    - Sensor(s) for reading temperature and humidity.
    - Controller that adjusts the humidity to ideal VPD ranges for the given growth stage the plants are in.
    - humidifier that is plumbed to be autofilled and responds to on/off requests from the Controller.
- Auto Soil Watering:
    - Sensors for reading the moisture level of the soil.
    - Blumat soakers for auto watering.  Setting of the carrot's valve based on the sensor reading.

# Goals
- Collect data for historical use.  Not for adjustments.  The VPD is "set and forget".  If there is a problem, VPD 

# VPD Buddy




# Managing Irrigation
Another thing to dial in is irrigation.  My strategy is to use Blumats.  To dial in the opening/closing of the Blumat valve, the soil the Blumat system will irrigate needs to be at the ideal wetness.  To do that, I'll calibrate some wifi enabled soil moisture sensors