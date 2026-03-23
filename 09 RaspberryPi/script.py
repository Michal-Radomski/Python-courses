import gpiod  # type: ignore[import-not-found]
import RPi.GPIO as GPIO  # type: ignore[import-not-found]
from gpiozero import LED  # type: ignore[import-not-found]

chip0 = gpiod.Chip("gpiochip0")
chip1 = gpiod.Chip("gpiochip1")
print("chip0, chip1:", chip0, chip1)

led = LED(17)
print("led:", chip0, chip1)


chip = gpiod.Chip("gpiochip0")

for i in range(0, 28):  # typical usable GPIO range
    try:
        line = chip.get_line(i)
        line.request(consumer="scan", type=gpiod.LINE_REQ_DIR_IN)
        val = line.get_value()
        print(f"GPIO {i}: {val}")
        line.release()
    except:  # noqa: E722
        pass

print("GPIO:", GPIO)
