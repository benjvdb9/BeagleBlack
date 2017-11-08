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
	pin('C4', on)
	pin('C5', on)
	pin('C1', off)
	pin('C8', off)
	
	pin('R4', off)
	pin('R5', off)
	pin('R1', on)
	pin('R8', on)
	time.sleep(delay)
	
	#Column 2 & 7
	pin('C1', on)
	pin('C8', on)
	pin('C2', off)
	pin('C7', off)
	
	pin('R1', off)
	pin('R8', off)
	pin('R2', on)
	pin('R7', on)
	time.sleep(delay)
	
	#Column 3 & 6
	pin('C2', on)
	pin('C7', on)
	pin('C3', off)
	pin('C6', off)
	
	pin('R2', off)
	pin('R7', off)
	pin('R3', on)
	pin('R6', on)
	time.sleep(delay)
	
	#Column 4 & 5
	pin('C3', on)
	pin('C6', on)
	pin('C4', off)
	pin('C5', off)
	
	pin('R3', off)
	pin('R6', off)
	pin('R4', on)
	pin('R5', on)
	time.sleep(delay)
