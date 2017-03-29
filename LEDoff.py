import Adafruit_BBIO.GPIO as GPIO
from initLED import initGPIOpins, inputUpperON
from initLED import inputLowerON, outputUpperOFF, outputLowerOFF

#turn off leds

initGPIOpins()
inputUpperOFF()
inputLowerOFF()
outputUpperOFF()
outputLowerOFF()