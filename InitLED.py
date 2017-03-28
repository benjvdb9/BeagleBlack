import Adafruit_BBIO.GPIO as GPIO

//initialize pins

def initGPIOpins():
	GPIO.setup("P8_12", GPIO.OUT)
	GPIO.setup("P8_14", GPIO.OUT)
	GPIO.setup("P8_16", GPIO.OUT)
	GPIO.setup("P8_18", GPIO.OUT)

	GPIO.setup("P8_20", GPIO.OUT)
	GPIO.setup("P8_22", GPIO.OUT)
	GPIO.setup("P8_24", GPIO.OUT)
	GPIO.setup("P8_26", GPIO.OUT)


	GPIO.setup("P8_11", GPIO.OUT)
	GPIO.setup("P8_13", GPIO.OUT)
	GPIO.setup("P8_15", GPIO.OUT)
	GPIO.setup("P8_17", GPIO.OUT)

	GPIO.setup("P8_19", GPIO.OUT)
	GPIO.setup("P8_21", GPIO.OUT)
	GPIO.setup("P8_23", GPIO.OUT)
	GPIO.setup("P8_25", GPIO.OUT)

def inputUpperON():
	GPIO.output("P8_12", GPIO.HIGH)
	GPIO.output("P8_14", GPIO.HIGH)
	GPIO.output("P8_16", GPIO.HIGH)
	GPIO.output("P8_18", GPIO.HIGH)

def inputLowerON():
	GPIO.output("P8_20", GPIO.HIGH)
	GPIO.output("P8_22", GPIO.HIGH)
	GPIO.output("P8_24", GPIO.HIGH)
	GPIO.output("P8_26", GPIO.HIGH)
	
def inputUpperOFF():
	GPIO.output("P8_12", GPIO.LOW)
	GPIO.output("P8_14", GPIO.LOW)
	GPIO.output("P8_16", GPIO.LOW)
	GPIO.output("P8_18", GPIO.LOW)

def inputLowerOFF():
	GPIO.output("P8_20", GPIO.LOW)
	GPIO.output("P8_22", GPIO.LOW)
	GPIO.output("P8_24", GPIO.LOW)
	GPIO.output("P8_26", GPIO.LOW)
	
def outputUpperON():
	GPIO.output("P8_11", GPIO.HIGH)
	GPIO.output("P8_13", GPIO.HIGH)
	GPIO.output("P8_15", GPIO.HIGH)
	GPIO.output("P8_17", GPIO.HIGH)
	
def outputLowerON():
	GPIO.output("P8_19", GPIO.HIGH)
	GPIO.output("P8_21", GPIO.HIGH)
	GPIO.output("P8_23", GPIO.HIGH)
	GPIO.output("P8_25", GPIO.HIGH)
	
def outputUpperOFF():
	GPIO.output("P8_11", GPIO.LOW)
	GPIO.output("P8_13", GPIO.LOW)
	GPIO.output("P8_15", GPIO.LOW)
	GPIO.output("P8_17", GPIO.LOW)

def outputLowerOFF():
	GPIO.output("P8_19", GPIO.LOW)
	GPIO.output("P8_21", GPIO.LOW)
	GPIO.output("P8_23", GPIO.LOW)
	GPIO.output("P8_25", GPIO.LOW)