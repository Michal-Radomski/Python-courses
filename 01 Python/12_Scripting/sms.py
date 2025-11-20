from twilio.rest import Client  # type: ignore

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="+...",
    body="test",
    to="+...",
)

print(message.sid)
