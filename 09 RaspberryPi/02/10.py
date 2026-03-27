# Not Tested!
# Interfacing RGB Led
# Todo: add GPIO.cleanup()

# Import the RPi.GPIO library for working with the Raspberry Pi GPIO pins
# Import the sleep function from the time module to introduce delays
from time import sleep

import RPi.GPIO as GPIO  # type: ignore[import-not-found]

# Define the GPIO pin numbers for red, green, and blue LEDs
rPin = 16
gPin = 20
bPin = 21

# Set the GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pins for output
GPIO.setup(16, GPIO.OUT)  # Red LED
GPIO.setup(20, GPIO.OUT)  # Green LED
GPIO.setup(21, GPIO.OUT)  # Blue LED


# Define a function to set the color of the RGB LED by turning on/off respective pins
def setColor(x, y, z):
    GPIO.output(rPin, x)  # Set the state of the red LED pin
    GPIO.output(gPin, y)  # Set the state of the green LED pin
    GPIO.output(bPin, z)  # Set the state of the blue LED pin


# Enter an infinite loop
while True:
    # Set the LED color to Red
    setColor(1, 0, 0)  # * Red -> Common Cathode ( if Common Anode setColor(0, 1, 1) )
    sleep(2)  # Pause for 2 seconds

    # Set the LED color to Green
    setColor(0, 1, 0)  # * Green -> Common Cathode ( if Common Anode setColor(1, 0, 1) )
    sleep(2)  # Pause for 2 seconds

    # Set the LED color to blue
    setColor(0, 0, 1)  # * Blue -> Common Cathode ( if Common Anode setColor(1, 1, 0) )
    sleep(2)  # Pause for 2 second
