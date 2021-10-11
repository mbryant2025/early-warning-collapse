
from twilio.rest import Client

#Account information; from Twilio
account_sid = "#"
auth_token = "#"

client = Client(account_sid, auth_token)

from_number = 0 #Number that will "send" the text message; from Twilio
to_number = 0 #Number that the message will be sent to

message = client.messages.create(body='testing3', from_=from_number, to=to_number)

print(message.sid)