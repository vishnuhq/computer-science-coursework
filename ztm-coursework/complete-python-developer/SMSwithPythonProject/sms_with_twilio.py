from twilio.rest import Client

account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1XXXXXXXXXX',
    body='Your message here.',
    to='+1XXXXXXXXXX'
)

print(message.sid)
