import RPi.GPIO as GPIO
import time

# This basic program will flash two LED's on and off alternately.

# Setting the output mode to digital
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

# Set the number of flashes:
numb_flashes = 10

# Set the duration of flashes (s):
flash_duration = 0.5

for i in range(numb_flashes):
    
    GPIO.output(13, True)
    GPIO.output(5, False)

    time.sleep(flash_duration)
    
    GPIO.output(13, False)
    GPIO.output(5, True)
    
    time.sleep(flash_duration)

# Clean up all the ports that have been used:
GPIO.cleanup()
