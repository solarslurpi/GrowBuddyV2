
# Water is Life
I learn so much each time I finish a grow.  My goal is to evolve my indoor Grow Buddy solution to include this knowledge.  The focus on this evolution is water.  Getting the right amount of water working for me in a grow room is where I need the most help for now.  I'll focus on lighting and other aspects after I evolve water automation.  There are two water sources I wish to smartly automate: humidity and watering the soil (I grow indoors in Living Soil).  

# What I am Building
- VPD Manager:
    - Sensor(s) for reading temperature and humidity.
    - Controller that adjusts the humidity to ideal VPD ranges for the given growth stage the plants are in.
    - humidifier that is plumbed to be autofilled and responds to on/off requests from the Controller.
- Auto Water:
    - Sensors for reading the moisture level of the soil.
    - Blumat soakers for auto watering.  Setting of the carrot's valve based on the sensor reading.

# Goals
- Collect data for historical use.  Not for adjustments.  The VPD is "set and forget".  If there is a problem, VPD 

# Managing Humidity



VPD (Vapor Pressure Deficit) and minimizing the chance for powdery mildew.  The last grow I had was outdoors.  Two of the plants got powdery mildew.  I spent many days searching and plucking out leaves.  Until we can get seeds with powdery mildew bread out, and even then! , my goal is to build an automated VPD system I'm calling VPD Buddy.  The environment will adjust to the three stages of growing - baby, vegetative, flower.
# VPD Buddy

<img src="https://docs.google.com/drawings/d/e/2PACX-1vTjks0iZHIZyD4VEdOo01_se0jn_CgJu9JUCee-rUhXBmFfykmObBkpqSUFBkOvnIdisiIzygPvDeZa/pub?w=599&amp;h=332">

- SnifferBuddy takes a reading

- mqtt is used as an API between devices and UI.  This way, any front end and any back end component can be evolved but still work within the system.  I look forward to evolution because at each stage it becomes more shockingly obvious I don't know what I'm doing.
- I decided to just set everything to work in Fahrenheight instead of Celcius for Temperature readings.  This is mostly because Fahrenheit is ingrained in my thinking (for worse or better).

# Managing Irrigation
Another thing to dial in is irrigation.  My strategy is to use Blumats.  To dial in the opening/closing of the Blumat valve, the soil the Blumat system will irrigate needs to be at the ideal wetness.  To do that, I'll calibrate some wifi enabled soil moisture sensors