# Weather-Station
Useful Weather station made in Raspberry pi and programmed in Python

I've made this project with a few sensors:

- ds18b20 Thermometer: A cheap hardware to measure temperatures.
- DHT11 Sensor: A Humidity + thermometer: I use it to measure humidity, in a future version i'd use this thermometer to measure the ground temperature.
- BMP180 Pressure module: It measures temperature, pressure and altitude, i used it mainly to measure pressure and altitude.
- WH-SP-WS01: An anemometer to measure wind speed.
- WH-SP-RG: A Rainmeter to measure Rainfall.

This weather station is made it fully in Python. It also has 2 versions, the station.py saves all measures in a sql server, station_csv.py saves it in an archive called data.csv.

Those measures will be added on a webpage and you'll be able to get the measurements in a telegram bot.


/SQL_Archives Folder:

It helps you to make a create the database that i'm using to commit measures in the SQL server, if you want use a csv file, you can ignore this folder.

Steps to make this database.

Install the mysql.connector from the internet with this command:

pip install mysql-connector-python

Then you can import this python module as:

import mysql.connector

Once you have installed this module. Run this scripts in this order:

1.- createdatabase.py -> This Make a SQL database called weather

2.- createtable.py -> This make a Table called data inside the weather database

3.- insertdata.py -> This file is not neccesary because it is running into station.py, it's just the code you need to import any code in the table created before.

