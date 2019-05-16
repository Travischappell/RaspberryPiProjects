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

import Adafruit_DHT
# Assign sensor type: [Adafruit_DHT.DHT11, Adafruit_DHT.DHT12, Adafruit_DHT.AM2302]
sensor = Adafruit_DHT.DHT11
pin = 4


"""
# Origina code; Not needed for my useage:
# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)
"""
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
https://github.com/Travischappell/RaspberryPiProjects.git
