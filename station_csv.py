# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:16:46 2021

@author: Marcial
"""

#Author: Marcial
#Version: 0.8
#Changes: commited in version.txt

from ds18b20 import DS18B20
from gpiozero import Button
import Adafruit_BMP.BMP085 as BMP085
import time
import sys
import Adafruit_DHT
import datetime
import math
import csv

#You can import all data in a csv file too, just quit # in the csv code.
#First of all, i have allowed my Station in a local mysql server to get all data from sensors.

#taken directly from w3c, easy and fast way to introduce data in a pre-made mysql database and table.

sql= "INSERT INTO data (date, temperature, pressure, humidity, altitude, wind, rain) VALUES (%s, %s, %s, %s, %s, %s, %s)"

#Instead using a python archive as a module for this sensors
#I have imported directly the ds18b20 and BMP085 python module.

sensor = DS18B20()
sensor2 = BMP085.BMP085()

#Added wind.py and rain.py archives.

#Both hardware are imported directly by the gpiozero python module.

interval = 5
wind_count=0
radius = 9.0 #cm
wind_interval = 5

#Adjustement factor for the anemometer (given in the instructions)

adjust_wind=1.18
rain_count=0

#Measures the times the anemometer is spinning.

def spin():
	global wind_count
	wind_count = wind_count + 1

def calculate_speed(time_sec):
	global wind_count
	perimeter = (2*math.pi)*radius
	rotations = wind_count / 2.0
	dist_km = (perimeter * rotations) / 100000

	kms = dist_km / time_sec
	kmh = kms * 3600

	return(kmh*adjust_wind)

def reset_wind():
    global wind_count
    wind_count = 0

wind_speed_sensor=Button(5)
wind_speed_sensor.when_pressed = spin
store_speeds=[]

#rain.py

rain_sensor = Button(6)
bucket_size = 0.2794
count = 0

def bucket_tipped():
	global rain_count
	rain_count = rain_count + 1
	#print(count*bucket_size)

def reset_rainfall():
	global rain_count
	rain_count=0

rain_count = 0
rain_sensor.when_pressed = bucket_tipped

#This meteo station takes data every ~30 seconds to take correctly wind and rain values.


while True:

    pressure = sensor2.read_pressure()
    altitude = sensor2.read_altitude()
    #This temperature will be added in the SQL database, 
    temperature_in_celsius = sensor.get_temperature()
    #The temperature given by the DHT sensor can be measured as ground temperature
    #Because this sensor is under the ds18b20 sensor and usually 
    humidity, temperature = Adafruit_DHT.read_retry(11,14)
    rainfall = rain_count * bucket_size
    wind=calculate_speed(wind_interval)

    now=datetime.datetime.now()

    
    print ("Pressure: %.2f hPa" % (pressure / 100.0))
    print ("Altitude: %.2f meters" % altitude)
    print ("Temperature:",temperature_in_celsius,"C")
    print ('Humidity: {1:0.1f} %'.format(temperature, humidity))
    print (time.ctime())
    print (wind, "km/h")
    print (wind)
    print (rainfall)
    print ('Record inserted')    
    print ('-----------------------------------------------')
    
    data = [time.ctime(), round(temperature,2), round(pressure,2),  round(altitude,2), humidity]

    with open('data.csv','a') as appendobj:
       append = csv.writer(appendobj)
       append.writerow(data)

    time.sleep(30)
    #Reset both wind and rain sensors to get a new measure.
    wind_count = 0
    reset_rainfall()	
