from gpiozero import Button
import time
import math
import datetime

interval=5
wind_count=0
radius= 9.0 #cm
wind_interval = 5
adjust=1.18
def spin():
    global wind_count
    wind_count = wind_count + 1
    #print("spin" + str(wind_count))

def calculate_speed(time_sec):
    global wind_count
    circunferencia_cm = (2*math.pi)*radius
    rotations = wind_count / 2.0
    dist_km = (circunferencia_cm * rotations) / 100000

    kms=dist_km / time_sec
    kmh= kms * 3600

    #speed = dist_cm / time_sec

    return(kmh*adjust)

def reset_wind():
    global wind_count
    wind_count = 0

wind_speed_sensor=Button(5)
wind_speed_sensor.when_pressed = spin
store_speeds=[]


while True:
    start_time = time.time()
    while time.time() - start_time <= interval:
        wind_start_time = time.time()

    wind_speed = calculate_speed(interval)
       
    final_speed=calculate_speed(wind_interval)
    store_speeds.append(final_speed)
    print(wind_speed)
    store_speeds=[]
    #wind_count=0
    #time.sleep(wind_interval)
    #print(calculate_speed(wind_interval), "km/h")

#spin()
