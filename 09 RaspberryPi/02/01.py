# Blinking LED Python Code

import time

import RPi.GPIO as GPIO  # type: ignore[import-not-found]

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

try:
    while True:
        GPIO.output(21, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(21, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:  # Handles Ctrl+C gracefully
    print("Stopped by user")
finally:
    GPIO.cleanup()  # Resets pin 21 to safe input state
