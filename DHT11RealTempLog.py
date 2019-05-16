# This file was built from the temperature example from the sensehat emulator
# also using the DHT11 example for Adafruit.
# documentation of instructions can be found here:
# https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/

import sys

import Adafruit_DHT
from time import sleep, strftime, time




def write_temp(temp):
    with open("/home/pi/Documents/Python/Script_Logs/roomtemplog.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

while True:
    temp = sense.temp
    tempf = (temp * 9/5) + 32
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
    write_temp(tempf)
    print(tempf)
    sleep(20)


