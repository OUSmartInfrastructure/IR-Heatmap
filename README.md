# This code was written by Dr. Julio Arauz, PhD and graduate student Riley Engle of Ohio University in Athens, Ohio.

IR Heatmap using the Adafruit AMG8833 IR board. It uses the Adafruit library for their IR sensor, as well as Numpy and SciPy.

This program uses the Adafruit AMG8833 IR Thermal Camera Breakout Board to gather IR data from objects in front of it. 
It also uses the Adafruit library located here:

https://github.com/adafruit/Adafruit_AMG88xx

And the tutorial setting up basic connectivity located here:

https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/overview

This project is a demonstration of the 8x8 sensor and displays a larger interpolated version to a webpage. The default code
contains the information for the final location where the sensor is mounted in Schoonover Center 009 at Ohio University in 
Athens, Ohio. This sensor is mounted above a window that users can view the webpage of the heatmap inside the room. 


The function of the files is as follows:

IR_Sensor.py

This program is the primary program. It uses the code from Adafruit with some modifications to pull sensor data, interpolate to 
a specified size, then save that information to a file called pixels.csv. This pixels.csv contains all information to be used 
with the other file in this repository (index.html). Please note, the formatting in the python script is intended for use with a 
csv file, but can be altered. 

This program contains a number of variable that can be updated, including the refresh rate

index.html

This file contains the JavaScript to pull the information from pixels.csv and place it on the web page in an svg object. 
The object draws a number of rectangles based on the number of entries in the pixels.csv file. 
This way, we can dynamically change the size in one location (the IR_Sensor.py script) while allowing the core 
functionality of the webpage remain the same. This page also contains a function to update the svg object with new data from the 
pixels.csv file. This number can be set with the variable declarations at the top of the script tags.

The webpage contains an image of where the sensor is mounted. The webpage positions the div that contains the svg object to be
located roughly where the sensor is located and will be gathering data (Heatmap.png).


