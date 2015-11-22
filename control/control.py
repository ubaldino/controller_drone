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
        """
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

        self.estaConfigurado = False

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
        """

    # metodo para establecer las velocidades de cada motor de 1 a 100
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

    # metodo para iniciar la configuarcion de los motores
    def iniciar( self ):
        sleep( 2 )
        GPIO.output( self.relay , 1 )
        sleep( self.tiempo ) #2.3
        print "configurando en alto los motoresen 4 seg."
        self.setMotores( self.valMaximo , self.valMaximo , self.valMaximo , self.valMaximo )
        sleep( 4 )
        print "configurando en bajo los motoresen 5 seg."
        self.setMotores( self.valMinimo , self.valMinimo , self.valMinimo , self.valMinimo )
        sleep( 5 )
        self.estaConfigurado = True

    # metodo para reiniciar los mo
    def reiniciar( self ):
        self.motor01.stop()
        self.motor02.stop()
        self.motor03.stop()
        self.motor04.stop()
        GPIO.output( self.relay , 0 )
        self.motor01.start( 0 )
        self.motor02.start( 0 )
        self.motor03.start( 0 )
        self.motor04.start( 0 )
        self.iniciar()

    def mapeo( valor ):
        if valor <= 0: valor = 0
        elif valor >= 100: valor = 100
        return ( ( valor * 0.05 ) + 4.5 )

    # metodo para uso en KeyboartInterrupt
    def interrumpir( self ):
        self.motor01.stop()
        self.motor02.stop()
        self.motor03.stop()
        self.motor04.stop()
        GPIO.output( self.relay , 0 )
        GPIO.cleanup()

    def test( self ):
        print "testd"

"""
try:
    print "inciciando en 2 seg"
    iniciar()
    while True:
        dutyC = float( raw_input( "Ingresa la velocidad entre (1 - 100): " ) )
        dutyC = mapeo( dutyC )
        setMotores( dutyC , dutyC , dutyC , dutyC )
except KeyboardInterrupt:
    interrumpir()
"""
