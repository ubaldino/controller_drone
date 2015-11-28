_autor_ = "Jorge Encinas"

from CanalPWM import CanalPWM
from time import sleep

class ControlRemoto:
	"""control PWM para 6 canales en Modo 2"""
	def __init__( self ):
		self.pwm1 = 16 # 36 # aleron
		self.pwm2 = 20 # 38 # elevador
		self.pwm3 = 21 # 40 # acelerador
		self.pwm4 = 13 # 33 # timon
		self.pwm5 = 19 # 35 # aux 1
		self.pwm6 = 26 # 37 # aux 2
		self.freq = 55 # frecuencia
		self.valMaximo = 10.6 # duty max
		self.valMinimo = 5.1  # duty min
		self.defecto = (self.valMaximo - self.valMinimo) / 2 + self.valMinimo # 50% entre el max y el min
		self.canal1 = CanalPWM(self.pwm1,self.freq,self.valMinimo,self.valMaximo,self.defecto)
		self.canal2 = CanalPWM(self.pwm2,self.freq,self.valMinimo,self.valMaximo,self.defecto)
		self.canal3 = CanalPWM(self.pwm3,self.freq,self.valMinimo,self.valMaximo,self.valMinimo)
		self.canal4 = CanalPWM(self.pwm4,self.freq,self.valMinimo,self.valMaximo,self.defecto)
		self.canal5 = CanalPWM(self.pwm5,self.freq,self.valMinimo,self.valMaximo,self.valMinimo)
		self.canal6 = CanalPWM(self.pwm6,self.freq,self.valMinimo,self.valMaximo,self.valMinimo)
	
	def reiniciar( self ):
		self.interrumpir()
		self.canal1.inicio()
		self.canal2.inicio()
		self.canal3.inicio()
		self.canal4.inicio()
		self.canal5.inicio()
		self.canal6.inicio()
		
	""" uso para except KeyboardInterrupt o similares"""
	def interrumpir( self ):
		self.canal1.interrumpir()
		self.canal2.interrumpir()
		self.canal3.interrumpir()
		self.canal4.interrumpir()
		self.canal5.interrumpir()
		self.canal6.interrumpir()
		
	def setAleron(self, vel):
		self.canal1.setDuty(vel)
	
	def setElevador(self, vel):
		self.canal2.setDuty(vel)
		
	def setAcelerador(self, vel):
		self.canal3.setDuty(vel)
		
	def setTimon(self, vel):
		self.canal4.setDuty(vel)
		
	def setAux1(self, vel):
		self.canal5.setDuty(vel)
		
	def setAux2(self, vel):
		self.canal6.setDuty(vel)
	
	def getAleron(self):
		return self.canal1.valor
	
	def getElevador(self):
		return self.canal2.valor
		
	def getAcelerador(self):
		return self.canal3.valor
		
	def getTimon(self):
		return self.canal4.valor
		
	def getAux1(self):
		return self.canal5.valor
		
	def getAux2(self):
		return self.canal6.valor
	
	def resetearValores(self):
		self.setAleron(50)
		self.setElevador(50)
		self.setAcelerador(0)
		self.setTimon(50)
		self.setAux1(0)
		self.setAux2(0)
	
	def testCanal(self):
		for i in range(50,100):
			self.setAleron(i)
			self.setElevador(i)
			self.setAcelerador(i)
			self.setTimon(i)
			self.setAux1(i)
			self.setAux2(i)
			sleep(0.05)
			print i
		for i in range(100,0,-1):
			self.setAleron(i)
			self.setElevador(i)
			self.setAcelerador(i)
			self.setTimon(i)
			self.setAux1(i)
			self.setAux2(i)
			sleep(0.05)
			print i
		self.resetearValores()
