import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)

try:
    time.sleep(2)
    while True:
        if GPIO.input(4):
            print("movement")
            time.sleep(2)
        time.sleep(0.1)
        
except:
    GPIO.cleanup()