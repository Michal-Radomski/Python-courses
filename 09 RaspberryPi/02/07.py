import smtplib
import time

import RPi.GPIO as GPIO  #  type: ignore[import-not-found]

# ========== CONFIGURATION ==========
sender = "<your_gmail@gmail.com>"
app_password = "<your_app_password_here>"
recipient = "<to_email@example.com>"
message = "Motion detected!"
# ==================================


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

# Connect and log in once, outside the loop
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(sender, app_password)

print("Motion-email script running...")

try:
    while True:
        x = GPIO.input(21)
        print("GPIO 21 state:", x)

        if x == 0:  # motion detected (PIR pulls low)
            try:
                s.sendmail(sender, recipient, message)
                print("📧 Email sent!")
            except Exception as e:
                print(f"❌ Failed to send email: {e}")

        time.sleep(2)  # debounce / delay

except KeyboardInterrupt:
    print("\nBye!")

finally:
    s.quit()
    GPIO.cleanup()
