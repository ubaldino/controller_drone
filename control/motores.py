#Fabrica de Software.
#Edgar E. Mamani Apaza.
#UMSS-Ing. Electronica
#refactor Jorge Encinas
# Implementacion Ubaldino Zurita

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

freq=50
dutyC=0

valMinimo = 4.5
valMaximo = 9.5

m1=17
m2=27
m3=22
m4=18

relay=23

tiempo = 2.3

GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
GPIO.setup(m3, GPIO.OUT)
GPIO.setup(m4, GPIO.OUT)

GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, 0)

motor01 = GPIO.PWM(m1, freq)
motor02 = GPIO.PWM(m2, freq)
motor03 = GPIO.PWM(m3, freq)
motor04 = GPIO.PWM(m4, freq)

motor01.start(0)
motor02.start(0)
motor03.start(0)
motor04.start(0)

print "inciciando en 2 seg"

def setMotores(vel01, vel02, vel03, vel04):
	motor01.ChangeDutyCycle(vel01)
	motor02.ChangeDutyCycle(vel02)
	motor03.ChangeDutyCycle(vel03)
	motor04.ChangeDutyCycle(vel04)


def arrancar():
        sleep(2)
        GPIO.output(relay, 1)
        sleep(tiempo)
	setMotores(valMaximo,valMaximo,valMaximo,valMaximo)
	sleep(4)
	print "configurando en bajo los motoresen 4 seg."
	setMotores(valMinimo,valMinimo,valMinimo,valMinimo)
	sleep(5)
	print "configurando en bajo los motoresen 5 seg."

def mapeo(valor):
	if valor<=0:
        	valor=0
        elif valor>=100:
                valor=100
        return ((valor*0.05)+4.5)

def interrumpir():
	motor01.stop()
        motor02.stop()
        motor03.stop()
        motor04.stop()
        GPIO.output(relay, 0)
        GPIO.cleanup()

try:
	arrancar()
	while True:
		dutyC=float(raw_input("Ingresa la velocidad entre (1 - 100): "))
		dutyC=mapeo(dutyC)
		setMotores(dutyC, dutyC, dutyC, dutyC)

except KeyboardInterrupt:
	interrumpir()
