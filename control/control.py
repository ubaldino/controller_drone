 #Fabrica de Software.
#Edgar E. Mamani Apaza.
#UMSS-Ing. Electronica
#refactor Jorge Encinas
# Implementacion Ubaldino Zurita

import RPi.GPIO as GPIO
from time import sleep


class Control:
    """control para el DRONE"""
    def __init__( self ):
        GPIO.setmode( GPIO.BCM )
        GPIO.setwarnings( False )

        self.freq = 50
        self.dutyC = 0

        self.valMinimo = 4.5
        self.valMaximo = 9.5

        self.m1 = 17
        self.m2 = 27
        self.m3 = 22
        self.m4 = 18

        self.relay = 23

        self.tiempo = 2.3

        GPIO.setup( self.m1 , GPIO.OUT )
        GPIO.setup( self.m2 , GPIO.OUT )
        GPIO.setup( self.m3 , GPIO.OUT )
        GPIO.setup( self.m4 , GPIO.OUT )

        GPIO.setup( self.relay , GPIO.OUT )
        GPIO.output( self.relay , 0 )

        self.motor01 = GPIO.PWM( self.m1 , self.freq )
        self.motor02 = GPIO.PWM( self.m2 , self.freq )
        self.motor03 = GPIO.PWM( self.m3 , self.freq )
        self.motor04 = GPIO.PWM( self.m4 , self.freq )

        self.motor01.start( 0 )
        self.motor02.start( 0 )
        self.motor03.start( 0 )
        self.motor04.start( 0 )


    def setMotores( self, vel01 , vel02 , vel03 , vel04 ):
        self.motor01.ChangeDutyCycle( vel01 )
        self.motor02.ChangeDutyCycle( vel02 )
        self.motor03.ChangeDutyCycle( vel03 )
        self.motor04.ChangeDutyCycle( vel04 )


    def arrancar( self ):
        sleep( 2 )
        GPIO.output( self.relay , 1 )
        sleep( self.tiempo )
        self.setMotores( valMaximo , valMaximo , valMaximo , valMaximo )
        sleep( 4 )
        print "configurando en bajo los motoresen 4 seg."
        self.setMotores( valMinimo , valMinimo , valMinimo , valMinimo )
        sleep( 5 )
        print "configurando en bajo los motoresen 5 seg."

    def mapeo( valor ):
        if valor <= 0: valor = 0
        elif valor >= 100: valor = 100
        return ( ( valor * 0.05 ) + 4.5 )

    def interrumpir():
        self.motor01.stop()
        self.motor02.stop()
        self.motor03.stop()
        self.motor04.stop()
        GPIO.output( self.relay , 0 )
        GPIO.cleanup()

    def test(self):
        print "test"

#control = Control()
#control.test()
"""

try:
    print "inciciando en 2 seg"
    arrancar()
    while True:
        dutyC = float( raw_input( "Ingresa la velocidad entre (1 - 100): " ) )
        dutyC = mapeo( dutyC )
        setMotores( dutyC , dutyC , dutyC , dutyC )
except KeyboardInterrupt:
    interrumpir()
"""