import datetime
import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleUtils import GoogleEvent, GoogleError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]
TOKENFILE = 'keys/token.json'
CREDFILE = 'keys/credentials.json'

class GoogleHelper:
    def __init__(self) -> None:
        self.refreshToken()

    def refreshToken(self):
        if os.path.exists(TOKENFILE):
            self._creds = Credentials.from_authorized_user_file(TOKENFILE, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self._creds or not self._creds.valid:
            if self._creds and self._creds.expired and self._creds.refresh_token:
                self._creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDFILE, SCOPES
                )
                self._creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKENFILE, "w") as token:
            token.write(self._creds.to_json())

    def getUpcomingEvents():
        pass

    def getEvent(self, eventId, calendar="primary"):
        if self._creds.valid:
            try:
                service = build("calendar", "v3", credentials=self._creds)
                event = service.events().get(calendarId=calendar, eventId=eventId).execute()
                return GoogleEvent(event)
            except HttpError as error:
                return GoogleError(error)
        else:
            print("not valid")
        pass

    def createEvent(self, event, calendar="primary"):
        try:
            service = build("calendar", "v3", credentials=self._creds)
            event = service.events().insert(calendarId=calendar, body=event).execute()
            return GoogleEvent(event)
        except HttpError as error:
            return GoogleError(error)