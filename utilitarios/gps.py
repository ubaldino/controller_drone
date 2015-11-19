import time
import serial
import re, os
import pynmea2

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 4800 ,
    timeout = 1
)

try:
	while 1 :
		time.sleep( 0.1 )
		linea = str( ser.readline() )
		if re.match( "\$GPGGA" , linea ):
			partes_linea = pynmea2.parse( linea )
			if partes_linea.latitude:
				os.system( "clear" )
				print "Latitude:\t %s"%partes_linea.latitude
				print "Longitude:\t %s"%partes_linea.longitude
				print "Altitude:\t %s"%partes_linea.altitude
				print "\n==========================================\n"
except KeyboardInterrupt:
	ser.flush()
	ser.close()
