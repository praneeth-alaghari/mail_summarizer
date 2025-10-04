import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

# Fetch secrets from environment variables
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")

def sendMessage(body, to):
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        body=f'Here is your daily email summary!\n\n {body}',
        to=f'whatsapp:+91{to}'
    )
    print("Message SID:", message.sid)

    # Check message status
    fetched_message = client.messages('SMa1659201a4c5eb560a70f4c9b9f781f8').fetch()
    print("Message Status:", fetched_message.status)