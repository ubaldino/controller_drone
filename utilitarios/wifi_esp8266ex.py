__author__ = 'ubaldino'

import serial

class ESP8266EX:
    def __init__(self):
        self.con =  serial.Serial( 1 , 38400 , timeout=0, parity=serial.PARITY_EVEN , rtscts=1 )

