from datetime import datetime, timedelta
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os
import json

with open("DATA/data.json", "r") as file:
    EMAILS = json.load(file)

SCOPES = ['https://www.googleapis.com/auth/calendar.events']
secret_key = 'API/client_secret_34040532511-s883ijjs7hn9t8kasancoqsjiot4v1ff.apps.googleusercontent.com.json'

def sendInvite(namesStr, date, time, description):
    names = [name.strip() for name in namesStr.split(",") if name.strip()]

    if not os.path.exists('API'):
        os.mkdir('API')

    token_path = 'API/token.json'

    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            secret_key, 
            SCOPES
        )
        creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    attendees = []
    for name in names:
        email = EMAILS.get(name)
        if email:
            attendees.append({'email': email})
        else:
            print (f"No email for {name}, skipping...")

    if not attendees:
        print("❌ No valid emails. Exiting.")
        return

    dt_start = datetime.strptime(f"2025/{date} {time}", "%Y/%m/%d %I:%M %p")
    dt_end = dt_start + timedelta(hours=1)

    event = {
        'summary': 'Series Shooting',
        'location': 'To be confirmed',
        'description': description,
        'start': {
            'dateTime': dt_start.isoformat(),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': dt_end.isoformat(),
            'timeZone': 'America/New_York',
        },
        'attendees': attendees,
        'reminders': {
            'useDefault': True,
        },
    }

    event_result = service.events().insert(
        calendarId='primary',
        body=event,
        sendUpdates='all'
    ).execute()

    return (f"Event created: {event_result.get('htmlLink')}")
