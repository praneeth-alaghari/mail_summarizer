
📧 Email Summarizer

Email Summarizer automates your inbox chaos! It fetches your recent Gmail emails, summarizes them using OpenAI, and sends the summary straight to your WhatsApp via Twilio. Stay updated without drowning in your inbox.

✨ Features

    📬 Gmail Integration – Fetch recent emails effortlessly via Google API.

    📝 Smart Summaries – OpenAI GPT turns email chaos into neat, bite-sized summaries.

    📱 WhatsApp Alerts – Receive your email summary directly on WhatsApp using Twilio.

    🔒 Secure Configuration – Store API keys and secrets safely in a .env file.

🛠 How It Works

    Authentication – Uses OAuth 2.0 to securely access your Gmail.
    
    Fetch Emails – Collects emails from the last 24 hours with sender, subject, and snippet.
    
    Summarization – Sends email data to OpenAI for a concise summary.
    
    WhatsApp Delivery – Sends the summary as a WhatsApp message via Twilio.


⚡ Prerequisites

    Python 3.x
    Gmail API enabled in Google Cloud
    Twilio account with WhatsApp messaging enabled
    OpenAI API key





🚀 Setup

    Libraries used :
        openai==0.28
        google
        google-api-python-client
        google-auth
        google-auth-oauthlib
        google-auth-httplib2
        pytz
        twilio
        python-dotenv

    # Clone the repo
    git clone <repository-url>
    cd <repository-folder>
    
    # Install dependencies
    pip install -r requirements.txt
    
    
    Configure your .env file:
    
    OPENAI_API_KEY=your_openai_api_key
    AUTH_TOKEN=your_twilio_auth_token
    ACCOUNT_SID=your_twilio_account_sid


    Run the app:
    
    python -m email_summarizer.email_summary

    Note : based on os, few adjustments to be done in terms of env/secrets configuration 

🎯 Conclusion

Email Summarizer keeps you in the loop without the overwhelm. It’s a neat combo of Gmail, OpenAI, and Twilio magic — all wrapped securely in environment variables.
