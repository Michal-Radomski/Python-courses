# Not Tested!
# Working with Buzzer
# Todo: add GPIO.cleanup()

import time

import RPi.GPIO as GPIO  # type: ignore[import-not-found]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
while True:
    GPIO.output(40, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(40, GPIO.LOW)
    time.sleep(1)
