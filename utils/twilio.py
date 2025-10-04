from twilio.rest import Client
from infra.twilio_auth_token import ACCOUNT_SID, AUTH_TOKEN
from infra.openai_secrets import OPENAI_API_KEY

def sendMessage(body, to):
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        body=f'Here is your daily email summary!\n\n {body}',
        to=f'whatsapp:+91{to}'
    )
    print("Message sent successfully. Message SID:", message.sid)