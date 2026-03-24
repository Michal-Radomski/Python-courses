# Working with DHT11 sensor code (Not Tested!)
# Todo: add GPIO.cleanup()
# python3 -m venv ~/myproject
# source ~/myproject/bin/activate
# pip3 install Adafruit_DHT
# or: pip install Adafruit_DHT --break-system-packages

import Adafruit_DHT  # type: ignore[import-not-found]

while True:
    h, t = Adafruit_DHT.read_retry(11, 21)
    print("Temp is", t)
    print("Humidity is", h)
