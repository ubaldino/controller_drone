# Fabrica de Software.
# Edgar E. Mamani Apaza. UMSS-Ing. Electronica
# Jorge Encinas Ing. Informatica UMSS.
# Implementacion Ubaldino Zurita.

import RPi.GPIO as GPIO
from time import sleep


class Control:
    """control para el DRONE"""
    def __init__( self ):
        GPIO.setmode( GPIO.BCM )
        GPIO.setwarnings( False )

        self.estaConfigurado = False

        self.freq = 50
        self.dutyC = 0

        self.valMinimo = 4 #4.5
        self.valMaximo = 10.5#9.5

        self.m1 = 17
        self.m2 = 27
        self.m3 = 22
        self.m4 = 18

        self.relay = 23

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
        if self.estaConfigurado:
            vel01 = self.mapeo( vel01 )
            vel02 = self.mapeo( vel02 )
            vel03 = self.mapeo( vel03 )
            vel04 = self.mapeo( vel04 )

        self.motor01.ChangeDutyCycle( vel01 )
        self.motor02.ChangeDutyCycle( vel02 )
        self.motor03.ChangeDutyCycle( vel03 )
        self.motor04.ChangeDutyCycle( vel04 )


    def iniciar( self ):
        self.motor01.start( 0 )
        self.motor02.start( 0 )
        self.motor03.start( 0 )
        self.motor04.start( 0 )
        sleep( 2 )
        GPIO.output( self.relay , 1 )
        sleep( 2.3 )
        self.setMotores( self.valMaximo , self.valMaximo , self.valMaximo , self.valMaximo )
        sleep( 4 )
        self.setMotores( self.valMinimo , self.valMinimo , self.valMinimo , self.valMinimo )
        sleep( 5 )
        self.estaConfigurado = True

    def mapeo( self, valor ):
        if valor < 0: valor = 0
        elif valor > 100: valor = 100
       # return ( valor * 0.05 ) + 8.5 """4.5"""
        return ( valor * ( self.valMaximo - self.valMinimo ) / 100 ) + self.valMinimo

    def interrumpir( self ):
        self.motor01.stop()
        self.motor02.stop()
        self.motor03.stop()
        self.motor04.stop()
        GPIO.output( self.relay , 0 )
        self.estaConfigurado = False
        #GPIO.cleanup()

    def test( self ):
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
