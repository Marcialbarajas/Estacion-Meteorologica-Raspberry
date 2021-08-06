import Adafruit_DHT
import time

SENSOR_DHT=Adafruit_DHT.DHT11
PIN_DHT=14

while True:
    humedad, temperatura = Adafruit_DHT.read(SENSOR_DHT, PIN_DHT)
    
    if humedad is not None and temperatura is not None:
        print("Temp{0:0.1f}C Hum={1:0.1f}%".format(temperatura, humedad))
    else:
        print("fallo")
    time.sleep(3)