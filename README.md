
# Water is Life
I learn so much each time I finish a grow.  My goal is to evolve my indoor Grow Buddy solution to include this knowledge.  The focus on this evolution is water.  __Getting the right amount of water working for me in a grow room is where I need the most help.__  There are two water sources I wish to smartly automate: the amount of water vapor in the air and the amount of water in the soil (I grow indoors in Living Soil).  

# What I am Building
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

<img src="https://docs.google.com/drawings/d/e/2PACX-1vTjks0iZHIZyD4VEdOo01_se0jn_CgJu9JUCee-rUhXBmFfykmObBkpqSUFBkOvnIdisiIzygPvDeZa/pub?w=599&amp;h=332">

- the VPD Controller gets temperature and RH (Relative Humidity) readings.
    - [SnifferBuddy](https://github.com/solarslurpi/GrowBuddy/blob/main/pages/SNIFFER_BUDDY.md) takes CO2 level, temperature, and humidity readings.  I will use the same SnifferBuddy I used last time.  It sends an mqtt message `tele/snifferbuddy/SENSOR` handled by the `growbuddy` broker with the payload `{"Time":"2022-09-06T08:52:59","ANALOG":{"A0":542},"SCD30":{"CarbonDioxide":814,"eCO2":787,"Temperature":71.8,"Humidity":61.6,"DewPoint":57.9},"TempUnit":"F"}` every twenty seconds. 
 ![snifferbuddy mqtt](images/mqttexplorer_snifferbuddy.jpg)   
            [MQTT Explorer](http://mqtt-explorer.com/) showing snifferbuddy messages.
    
     _Note: I've been using a scd30 (or scd40) because these sensors have awesome CO2 detection._
- The VPD Controller knows the range of ideal values for the VPD given the growth stage the plants are in. The source for the ideal VPD values is Pulse's[] _The Ultimate Vapor Pressure Deficit (VPD) Guide_](https://pulsegrow.com/blogs/learn/vpd)
.
# Managing Irrigation
Another thing to dial in is irrigation.  My strategy is to use Blumats.  To dial in the opening/closing of the Blumat valve, the soil the Blumat system will irrigate needs to be at the ideal wetness.  To do that, I'll calibrate some wifi enabled soil moisture sensors