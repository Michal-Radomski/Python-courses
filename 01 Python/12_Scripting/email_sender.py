import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # or os.path

html = Template(Path("index.html").read_text())

email = EmailMessage()
email["from"] = "Universe"
email["to"] = "<to email address>"
email["subject"] = "You are cool"

email.set_content(html.substitute({"name": "Just Me"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("<your email address>", "<your password>")
    smtp.send_message(email)
    print("all good boss!")
