_autor_ = "Jorge Encinas"

from CanalPWM import CanalPWM
from time import sleep
import serial

class ControlRemoto:
	"""control PWM para 6 canales en Modo 2"""
	def __init__( self ):
		""""
		self.ser = serial.Serial(
		port='/dev/ttyACM0',
		baudrate = 9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
		)"""
		
		self.ser = serial.Serial( port='/dev/ttyACM0', baudrate = 9600 )
		self.throttle = 0
		self.roll = 50
		self.pitch = 50
		self.yaw = 50
		self.flightMode = 0
		self.accessory0 = 0
	
		#self.bcm1 = 16 # pin 36 # aleron roll 2
		#self.bcm2 = 20 # pin 38 # elevador pitch
		#self.bcm3 = 21 # pin 40 # acelerador throle 1
		#self.bcm4 = 13 # pin 33 # timon yaw
		#self.bcm5 = 19 # pin 35 # aux 1 swith 1 flight mode
		#self.bcm6 = 26 # pin 37 # aux 2 swith 2
	
	def writeSerial(self, cad):
		self.ser.write(cad)
	
	def reiniciar( self ):
		print "no implementado reinicar"
	""" uso para except KeyboardInterrupt o similares"""
	def interrumpir( self ):
		print "no implementado interrumpir"
		
	def setAleron(self, vel):
		self.roll = vel
		self.writeSerial( 'r' + str(vel))
	
	def setElevador(self, vel):
		self.pith = vel
		self.writeSerial( 'p' + str(vel))
		
	def setAcelerador(self, vel):
		self.throttle = vel
		self.writeSerial( 't' + str(vel))
		
	def setTimon(self, vel):
		self.yaw = vel
		self.writeSerial( 'y' + str(vel))
		
	def setAux1(self, vel):
		self.flightMode = vel
		self.writeSerial( 'f' + str(vel))
		
	def setAux2(self, vel):
		self.accessory0 = vel
		self.writeSerial( 'a' + str(vel))
	
	def getAleron(self):
		return self.roll.valor
	
	def getElevador(self):
		return self.pitch.valor
		
	def getAcelerador(self):
		return self.throttle.valor
		
	def getTimon(self):
		return self.yaw.valor
		
	def getAux1(self):
		return self.flightMode.valor
		
	def getAux2(self):
		return self.accessory0.valor
	
	
	def resetearValores(self):
		self.throttle = 0
		self.roll = 50
		self.pitch = 50
		self.yaw = 50
		self.flightMode = 0
		self.accessory0 = 0
"""
	def testCanal(self):
		for i in range(50,100):
			self.throttle = i
			self.roll = i
			self.pitch = i
			self.yaw = 50
			self.flightMode = 0
			self.accessory0 = 0
			sleep(0.05)
			print i
		for i in range(100,0,-1):
			self.throttle = 0
			self.roll = 50
			self.pitch = 50
			self.yaw = 50
			self.flightMode = 0
			self.accessory0 = 0
			sleep(0.05)
			print i
		self.resetearValores()
"""
