import RPi.GPIO as GPIO
from time import sleep

touch = 18
go = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(touch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button='up'
relay='off'

while True:
    if (button=='up'   and   relay=='off'):
        if not GPIO.input(touch):
            GPIO.setup(go,GPIO.LOW)
            button='down'; 
            relay='on'
    elif (button=='down' and   relay=='on'):
        if GPIO.input(touch):
            button='up'
    elif (button=='up'   and   relay=='on'):
        if not GPIO.input(touch):
            GPIO.setup(go,GPIO.HIGH)
            button='down'
            relay='off'
    elif (button=='down' and   relay=='off'):
        if GPIO.input(touch):
            button='up'
    sleep(0.1)
    
    