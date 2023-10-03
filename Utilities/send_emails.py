from __future__ import print_function
import base64
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

Credentials_JSON = '/Users/chakrapani/AIWeGuardAPIs/Utilities/credentials.json'
Token_JSON = '/Users/chakrapani/AIWeGuardAPIs/Utilities/token.json'

creds = None
if os.path.exists(Token_JSON):
    creds = Credentials.from_authorized_user_file(Token_JSON, SCOPES)

# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        from google_auth_oauthlib.flow import InstalledAppFlow

        flow = InstalledAppFlow.from_client_secrets_file(Credentials_JSON, SCOPES)
        creds = flow.run_local_server(port=0)

    # Save the credentials for the next run in the Utilities directory
    with open(Token_JSON, 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)
sender = 'qateam126@gmail.com'  # Change this to your Gmail address
subject = "API Test Report"
recipients = ['chakrapani.bandhu@wenable.com']  # Change this to the recipient's email addresses
message_text = "Please find the report of pyscripts executed"

# Read the file path from the command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 send_emails.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

def create_message_with_attachment(recipient, file_path):
    message = MIMEMultipart()
    message['to'] = recipient
    message['from'] = sender
    message['subject'] = subject

    text = MIMEText(message_text)
    message.attach(text)

    # Attach the HTML report file
    with open(file_path, 'rb') as file:
        attachment = MIMEApplication(file.read(), _subtype="html")
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
        message.attach(attachment)

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, message):
    try:
        message = service.users().messages().send(userId='me', body=message).execute()
        print('\nEmail sent successfully. Message Id: %s' % message['id'] + "\n")
    except Exception as error:
        print('An error occurred while sending the email:', error)

# Send the email with the specified report file path to each recipient
for recipient in recipients:
    message = create_message_with_attachment(recipient, file_path)
    send_message(service, message)
