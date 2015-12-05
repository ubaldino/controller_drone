_autor_ = "Jorge Encinas"

import RPi.GPIO as GPIO

class CanalPWM:
	"""control PWM"""
	def __init__( self , pinBCM ,periodo, minimo, maximo, defecto):
		self.pinBCM = pinBCM
		self.periodo = periodo
		self.minimo = minimo
		self.maximo = maximo 
		self.valor = defecto # % para dudy en 0 - 100
		self.defectoDuty = self.mapeo( defecto ) # % para dudy cycle
		self.inicio()
		
	def inicio( self ):
		GPIO.setmode( GPIO.BCM )
		GPIO.setwarnings( False )
		GPIO.setup( self.pinBCM , GPIO.OUT )
		frecuencia = 1 / self.periodo
		self.pwm = GPIO.PWM( self.pinBCM , frecuencia )
		self.pwm.start( self.defectoDuty )
	
	""" Valores entre 0 y 100"""
	def setDuty( self, valor):
		self.valor = valor
		self.pwm.ChangeDutyCycle( self.mapeo( valor ) )
	
	def mapeo( self, valor ):
		if valor < 0: valor = 0
		elif valor > 100: valor = 100
		return ( valor * ( self.maximo - self.minimo ) + self.minimo * 100 ) / self.periodo
		
	def interrumpir( self ):
		self.pwm.stop()
		#self.pwm.ChangeDutyCycle( self.defectoDuty )# posible solucion al estado de pwm en openpilot cuando ocurre algun error o cambiar a un metodo de pwm actual a bajo progresivamente en un tiempo
		GPIO.cleanup()
