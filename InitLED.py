import Adafruit_BBIO.GPIO as GPIO

#initialize pins

def getpin(P):
	dict = {'R1':'44', 'R2':'26', 'R3':'46', 'R4':'65', 'R5':'63', 'R6':'37', 'R7':'33', 'R8':'61'
			'C1':'45', 'C2':'23', 'C3':'47', 'C4':'27', 'C5':'22', 'C6':'62', 'C7':'36', 'C8':'32'}
	
	try:
		pin = dict[P]
	except:
		pin = P
	#RRR
	return pin
	
def pinconf(P, dir):
	pin = getpin(P)
	
	if not os.path.exists('/sys/class/gpio/gpio' + pin):  
	    with open('/sys/class/gpio/export', 'w') as file:  
	        file.write(pin)  
	with open('/sys/class/gpio/gpio'+ pin +'/direction', 'w') as file:  
	    file.write(dir)
	
def pin(P, state):
	pin = getpin(P)
	
	if (state == 'on'):
		frt = 1
	else:
		frt = 0
		
	with open('/sys/class/gpio/gpio'+ pin +'/value', 'w') as file:  
	    file.write(frt)
 
def readpin(P):
	pin = getpin(P)
	
	if not os.path.exists('/sys/class/gpio/gpio' + pin):  
	    with open('/sys/class/gpio/export', 'w') as file:  
	        file.write(pin)
	with open('/sys/class/gpio/gpio'+ pin +'/value', 'w') as file:  
	    val = file.read()
		return val

def initGPIOpins():
	pinconf('R1', out)
	pinconf('R2', out)
	pinconf('R3', out)
	pinconf('R4', out)

	pinconf('R5', out)
	pinconf('R6', out)
	pinconf('R7', out)
	pinconf('R8', out)


	pinconf('C1', out)
	pinconf('C2', out)
	pinconf('C3', out)
	pinconf('C4', out)

	pinconf('C1', out)
	pinconf('C2', out)
	pinconf('C3', out)
	pinconf('C4', out)

def inputUpperON():
	pin('R1', on)
	pin('R2', on)
	pin('R3', on)
	pin('R4', on)

def inputLowerON():
	pin('R5', on)
	pin('R6', on)
	pin('R7', on)
	pin('R8', on)
	
def inputUpperOFF():
	pin('R1', off)
	pin('R2', off)
	pin('R3', off)
	pin('R4', off)

def inputLowerOFF():
	pin('R5', off)
	pin('R6', off)
	pin('R7', off)
	pin('R8', off)
	
def outputUpperON():
	pin('C1', on)
	pin('C2', on)
	pin('C3', on)
	pin('C4', on)
	
def outputLowerON():
	pin('C5', on)
	pin('C6', on)
	pin('C7', on)
	pin('C8', on)
	
def outputUpperOFF():
	pin('C1', off)
	pin('C2', off)
	pin('C3', off)
	pin('C4', off)

def outputLowerOFF():
	pin('C5', off)
	pin('C6', off)
	pin('C7', off)
	pin('C8', off)