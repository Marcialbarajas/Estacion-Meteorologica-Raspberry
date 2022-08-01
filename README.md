# Weather-Station

Estación meteorológica funcional montada en Raspberry Pi y programada en Python.

He hecho este proyecto con los siguientes sensores:

- Ds18b20 Thermometer: Termómetro simple para medir temperatura del aire.
- 
- DHT11 Sensor: Sensor que mide humedad y temperatura: Usado para medir humedad, en un futuro el termómetro que viene podría ser incluido para medir la temperatura del suelo.
- 
- BMP180 Módulo de Presión: Este módulo mide presión, temperatura y altitud, para este proyecto es usado para medir presión y altitud (aunque se mantenga constante).
- 
- WH-SP-WS01: Anemómetro para medir la velocidad del viento.
- WH-SP-RG: Un pluviómetro para medir la cantidad de precipitación.

Esta estación meteorológica está hecha casi al completo en Python, también tiene dos versiones: 
-El fichero station.py guarda las medidas en un servidor local sql
-El fichero station_csv.py guarda las medidas en un archivo llamado data.csv

Las medidas tomadas serán añadidas a una página web y será posible recibir notificaciones vía telegram


Carpeta de archivos SQL:

Esto ayuda a crear una base de datos tal y como la que se está usando para añadir las medidas en el servidor SQL local, aunque si se desea usar el fichero .csv, ignora esta carpeta.

Pasos para crerar esta base de datos:

-Instala el módulo de Python mysql.connector desde internet con este comando para python:

- pip install mysql-connector-python

Entonces ya se podrá importar el módulo de Python como:

import mysql.connector

Una vez que tengas instalado este módulo, corre estos scripts en este orden:

1.- createdatabase.py -> Hace una base de datos SQL llamada weather

2.- createtable.py -> Hace una tabla llamada data dentro de la base de datos weather

3.- insertdata.py -> Este fichero no es necesario porque está dentro del archivo station.py, es solo el código que se necesita para importar cualquier dato en la tabla creada anteriormente.
