import Adafruit_BBIO.GPIO as GPIO
from initLED import initGPIOpins, inputUpperON
from initLED import inputLowerON, outputUpperOFF, outputLowerOFF
import time

#initialize leds
initGPIOpins()
inputUpperOFF()
inputLowerOFF()
outputUpperOFF()
outputLowerOFF()

while True:
	inputUpperON()
	outputLowerON()
	time.sleep(1)
	
	outputUpperON()
	outputUpperOFF()
	time.sleep(1)
	
	inputUpperOFF()
	inputLowerON()
	outputUpperOFF()
	outputLowerON()
	time.sleep(1)
	
	outputUpperON()
	outputUpperOFF()
	time.sleep(1)