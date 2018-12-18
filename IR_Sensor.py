#This code was written by Dr. Julio Arauz, PhD and graduate student Riley Engle
#Edited by graduate student Christopher M Johnston
#at Ohio University in Athens, Ohio

from Adafruit_AMG88xx import Adafruit_AMG88xx
import math, time, sys
from scipy.interpolate import griddata
import numpy as np

def map(x, a, b, c, d):
	return ((x-a) / ((b-a)*(d-c))) + c

def formatData(list, row):
	i = 0
	data = ""
	while i < len(list[row]):
		data = data + str(row) + ', '+str(i)+', '+str(list[row][i]) +'\n'
		i+=1
	return data

def average(pixels):
	l = len(pixels)
	t = 0
	for x in pixels:
		t = t+x
	return float(t/l)

fn = '/var/www/html/data/pixels.csv' #File of output

sensor = Adafruit_AMG88xx()
MINTEMP = 22
MAXTEMP = 30
rangeMin = 0
rangeMax = 1

#size of new board
h = 64
w = 64
#8 is due to the number of pixels on board; 8x8 = 64 pixels
points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]

i = 0
go = 1
#Delay before getting next reading
refresh = 0.05

while go:
	#Allow for Sensor to initialize
	time.sleep(refresh)

	#Get Pixel readings and map them for use with D3
	pixels = sensor.readPixels()
	pixels = [map(float(p), MINTEMP, MAXTEMP, rangeMin, rangeMax) for p in pixels]

	#Write average temp to file

	#Create Grid of specified size -TODO make variables???
	xi, yi = np.mgrid[0:7:32j, 0:7:32j]

	#Interpolate
	bicubic = griddata(points, pixels, (xi,yi), method='cubic')

	#Write Data

	f = open(fn,'w')
	f.write('x,y,value\n')
	i=0

	while i < len(bicubic):
		data = formatData(bicubic,i)
		f.write(data)
		i+=1

	f.close()
