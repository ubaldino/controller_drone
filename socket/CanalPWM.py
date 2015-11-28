_autor_ = "Jorge Encinas"

import RPi.GPIO as GPIO

class CanalPWM:
	"""control PWM"""
	def __init__( self , bcm ,frecuencia, min, max, defecto):
		self.pin = bcm
		self.freq = frecuencia
		self.valMinimo = min
		self.valMaximo = max
		self.defecto = defecto
		self.inicio()
	
	def setDuty( self, vel):
		self.valor = vel
		self.pwm.ChangeDutyCycle( self.mapeo( vel ) )
	
	def mapeo( self, valor ):
		if valor < 0: valor = 0
		elif valor > 100: valor = 100
		return ( valor * ( self.valMaximo - self.valMinimo ) / 100 ) + self.valMinimo

	def inicio( self ):
		GPIO.setmode( GPIO.BCM )
		GPIO.setwarnings( False )
		GPIO.setup( self.pin , GPIO.OUT )
		self.pwm = GPIO.PWM( self.pin , self.freq )
		self.pwm.start( self.defecto )
		self.valor = ( self.defecto - self.valMinimo ) / ( ( self.valMaximo - self.valMinimo ) / 100 )
		
	def interrumpir( self ):
		self.pwm.stop()
		GPIO.cleanup()
