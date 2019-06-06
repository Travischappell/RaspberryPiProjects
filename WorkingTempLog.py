#This it the example temp READER from Adafruit for the DHT temp sensor
#
#Its been modfied for my project.

#Project Intent
# Part I
#   1. Temperature and Humidity are pulled at a set interaval
#   2. The results of the sensor are SAVED to a csv file along with date and time
# Part II
#   1. If room temperature is above a threshold, send signal to turn on the A/C
#   2. Turn-off signal is sent when temperate drops BELOW threshold, or after a certain time
#   3. Only runs at certain times per day (middle of day)


import sys
from time import sleep, strftime, time
import Adafruit_DHT

# Assign sensor type: [Adafruit_DHT.DHT11, Adafruit_DHT.DHT12, Adafruit_DHT.AM2302]
sensor = Adafruit_DHT.DHT11
pin = 4


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

def write_temp(temperature, humidity):
    with open("/home/pi/Documents/Python/Script_Logs/roomtemplog.csv", "a") as log:
        log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temperature),str(humidity)))

iteration = 0
runtime = int(input("How many minutes to read? "))

while iteration < runtime:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
# Un-comment the line below to convert the temperature to Fahrenheit.
    temperature = temperature * 9/5.0 + 32
    write_temp(temperature, humidity)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    sleep(60)
    iteration += 1

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
