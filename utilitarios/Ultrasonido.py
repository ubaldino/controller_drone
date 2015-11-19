import RPi.GPIO as GPIO  
import time                
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
mode=GPIO.getmode    
GPIO_TRIGGER = 22          
GPIO_ECHO    = 18           
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  
GPIO.setup(GPIO_ECHO,GPIO.IN)      
GPIO.output(GPIO_TRIGGER,False)   

try:
    while True:    
        GPIO.output(GPIO_TRIGGER,True)  
        time.sleep(0.00001)             
        GPIO.output(GPIO_TRIGGER,False) 
        start = time.time()
        while GPIO.input(GPIO_ECHO)==0:
            start = time.time()         
        while GPIO.input(GPIO_ECHO)==1: 
            stop = time.time()          
        elapsed = stop-start            
        distance =round ((elapsed * 34300)/2)   
        print distance                  
        time.sleep(.3)    
except KeyboardInterrupt:                
    print "quit"                         
    GPIO.cleanup()                       
