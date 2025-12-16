To add Mailgun to a Flask API, sign up at Mailgun, verify a sending domain to get your API key and domain endpoint, then use
the `requests` library to send emails via HTTP POST. Store credentials securely in environment variables loaded via
`python-dotenv`. This enables transactional emails like notifications or resets in your API routes.[1]

## Prerequisites

Install dependencies and set up credentials.

```
pip install flask requests python-dotenv
```

Create `.env` with:

```
MAILGUN_API_KEY=your_api_key_here
MAILGUN_DOMAIN=your-domain.mailgun.org
MAILGUN_API_URL=https://api.mailgun.net/v3/your-domain.mailgun.org
```

Load with `load_dotenv()` in your app.[1]

## Sending Emails

Define a reusable function for POST requests to Mailgun.

```python
import os
import requests
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app = Flask(__name__)

def send_email(to_email, subject, text, from_email="noreply@your-domain.mailgun.org"):
    return requests.post(
        os.environ.get('MAILGUN_API_URL'),
        auth=("api", os.environ.get('MAILGUN_API_KEY')),
        data={"from": from_email,
              "to": [to_email],
              "subject": subject,
              "text": text})
```

Use HTML by replacing `"text"` with `"html"`.[1]

## API Route Example

Integrate into a route, like a contact form handler.

```python
@app.route('/send-email', methods=['POST'])
def api_send_email():
    data = request.json
    response = send_email(data['to'], data['subject'], data['message'])
    if response.status_code == 200:
        return {'status': 'success'}, 200
    return {'status': 'error'}, 500
```

Check `response.status_code` for success (200).[1]

## Best Practices

- Handle errors with try-except around requests.
- Use async with `aiohttp` for high-volume sends.
- Test in Mailgun sandbox before production.[1]

[1](https://techmonger.github.io/26/flask-mailgun/) [2](https://www.youtube.com/watch?v=1WXPqd1NDBk)
[3](https://mailtrap.io/blog/flask-email-sending/)
[4](https://www.mailgun.com/blog/it-and-engineering/send-email-using-python/)
[5](https://www.mailgun.com/blog/dev-life/build-transactional-workflows-for-abandoned-cart-notifications/)
[6](https://github.com/shubhtoy/Bulk-Email-Sender-Flask-Mailgun)
[7](https://stackoverflow.com/questions/13079755/flask-on-heroku-with-mailgun-config-issues)
[8](https://stackoverflow.com/questions/56485617/mail-gun-email-not-working-in-flask-on-google-app-engine)
[9](https://mailtrap.io/blog/flask-send-email-gmail/)
[10](https://community.latenode.com/t/trouble-accessing-email-data-sent-by-mailgun-to-python-flask-application/19021)
