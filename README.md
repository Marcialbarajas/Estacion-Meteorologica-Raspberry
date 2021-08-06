# Weather-Station
Useful Weather station made in Raspberry pi and programmed in Python

I've made this project with a few sensors:

- ds18b20 Thermometer: A cheap hardware to measure temperatures.
- DHT11 Sensor: A Humidity + thermometer: I use it to measure humidity, in a future version i'd use this thermometer to measure the ground temperature.
- BMP180 Pressure module: It measures temperature, pressure and altitude, i used it mainly to measure pressure and altitude.
- WH-SP-WS01: An anemometer to measure wind speed.
- WH-SP-RG: A Rainmeter to measure Rainfall.

This weather station is made it fully in Python. It also has 2 versions, the station.py saves all measures in a sql server, station_csv.py saves it in an archive called data.csv.

This is a WIP project. I'm still developing and improving.
