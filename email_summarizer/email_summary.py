import os.path
import pickle
import datetime
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from llm_dir.openai_llm import get_openai_response
from utils.twilio import sendMessage
from dotenv import load_dotenv
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Get the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

token_path = os.path.join(BASE_DIR, '..', 'token.pickle')  # adjust if needed
token_path = os.path.abspath(token_path)


load_dotenv(f"{BASE_DIR}/.env")



def authenticate_gmail():
    credentials = None

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'infra/gmail_api_credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0, success_message='The authentication flow has completed successfully.')
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return credentials

def fetch_recent_emails(service):
    yesterday = datetime.datetime.now(pytz.UTC) - datetime.timedelta(days=1)
    query = f'after:{yesterday.strftime("%Y/%m/%d")}'
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    emails = []
    
    for msg in messages:
        msg_detail = service.users().messages().get(userId='me', id=msg['id']).execute()
        email_data = {}
        email_data['snippet'] = msg_detail['snippet']
        email_data['from'] = next(header['value'] for header in msg_detail['payload']['headers'] if header['name'] == 'From')
        email_data['subject'] = next(header['value'] for header in msg_detail['payload']['headers'] if header['name'] == 'Subject')
        email_data['date'] = next(header['value'] for header in msg_detail['payload']['headers'] if header['name'] == 'Date')

        emails.append(email_data)

    return emails


def get_summary():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    
    recent_emails = fetch_recent_emails(service)
    
    prompt = f'''Summarize the following emails in 5-10 sentences:\n {recent_emails}, providing a clear and concise overview. Format the summary in a visually appealing way, with each point on a separate line. Include relevant details and key information to give a comprehensive understanding of the emails.

                - Summarize the main points of the emails.
                - Focus on the key information and important details.
                - Use a clear and concise writing style.
                - Organize the summary in a logical and easy-to-read format.
                - Highlight any important actions or next steps mentioned in the emails.
                - Ignore promotional emails or newsletters.
                - No need to bold any content
              '''
    
    # Directly pass the fetched emails to the OpenAI function
    summary = get_openai_response(prompt)

    return summary


if __name__ == "__main__":
    summary = get_summary()
    # Print the output from the OpenAI response
    print("Summary of Recent Emails Received in the Last 24 Hours:")
    print(summary)

    sendMessage(summary, "9573340942")  # Replace with the actual phone number
    
    # Uncomment below to print recent emails if needed
    # print("Recent Emails Received in the Last 24 Hours:")
    # print(f"{'Sender Email':<30} {'Received Time':<20} {'Subject':<50}")
    # print("=" * 100)
    # for email in recent_emails:
    #     print(f"{email['from']:<30} {email['date']:<20} {email['subject']:<50}")

