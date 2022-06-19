from twilio.rest import Client
#You will get your individual ACCOUNT SID and ACCOUNT TOKEN when you sign upmto Twilio using the link in https://www.twilio.com/docs/sms 
ACCOUNT_SID = "SID"
ACCOUNT_TOKEN ="TOKEN"
PHONE_NUMBER = "PHONE NUMER"

client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass

    def send_message(self, text):
        message = client.messages.create(
            body=text,
            from_= PHONE_NUMBER,
            to='+my NUMBER',

        )

        print(message.sid)

