import Adafruit_BBIO.GPIO as GPIO
from initLED import initGPIOpins, inputUpperON
from initLED import inputLowerON, outputUpperOFF, outputLowerOFF
import time

#initialize leds
initGPIOpins()

#led off
inputUpperOFF()
inputLowerOFF()
outputUpperON()
outputLowerON()

delay = 0.1

while True:
	#Column 1 & 8
	GPIO.output("P8_17", GPIO.HIGH)
	GPIO.output("P8_19", GPIO.HIGH)
	GPIO.output("P8_11", GPIO.LOW)
	GPIO.output("P8_25", GPIO.LOW)
	
	GPIO.output("P8_18", GPIO.LOW)
	GPIO.output("P8_20", GPIO.LOW)
	GPIO.output("P8_12", GPIO.HIGH)
	GPIO.output("P8_26", GPIO.HIGH)
	time.sleep(delay)
	
	#Column 2 & 7
	GPIO.output("P8_11", GPIO.HIGH)
	GPIO.output("P8_25", GPIO.HIGH)
	GPIO.output("P8_13", GPIO.LOW)
	GPIO.output("P8_23", GPIO.LOW)
	
	GPIO.output("P8_12", GPIO.LOW)
	GPIO.output("P8_26", GPIO.LOW)
	GPIO.output("P8_14", GPIO.HIGH)
	GPIO.output("P8_24", GPIO.HIGH)
	time.sleep(delay)
	
	#Column 3 & 6
	GPIO.output("P8_13", GPIO.HIGH)
	GPIO.output("P8_23", GPIO.HIGH)
	GPIO.output("P8_15", GPIO.LOW)
	GPIO.output("P8_21", GPIO.LOW)
	
	GPIO.output("P8_14", GPIO.LOW)
	GPIO.output("P8_24", GPIO.LOW)
	GPIO.output("P8_16", GPIO.HIGH)
	GPIO.output("P8_22", GPIO.HIGH)
	time.sleep(delay)
	
	#Column 4 & 5
	GPIO.output("P8_15", GPIO.HIGH)
	GPIO.output("P8_21", GPIO.HIGH)
	GPIO.output("P8_17", GPIO.LOW)
	GPIO.output("P8_19", GPIO.LOW)
	
	GPIO.output("P8_16", GPIO.LOW)
	GPIO.output("P8_22", GPIO.LOW)
	GPIO.output("P8_18", GPIO.HIGH)
	GPIO.output("P8_20", GPIO.HIGH)
	time.sleep(delay)