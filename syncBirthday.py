from notionHelper import NotionUtils
from googleUtils import GoogleEvent
from googleHelper import GoogleHelper

BIRTHDAY_CALENDAR = '963f9f32449806b9e2227be46a906f3d68b0aae9898d35e93909012d96298751@group.calendar.google.com'
birthdays = NotionUtils.getBirthdays()
google = GoogleHelper()
for birth in birthdays:
    if birth.googleId is None:
        gogEvent = GoogleEvent()
        gogEvent.summary = birth.name
        gogEvent.start = {
            "date" : birth.actualDate.strftime("%Y-%m-%d")
        }
        gogEvent.end = {
            "date" : birth.actualDate.strftime("%Y-%m-%d")
        }
        newGoogleEvent = google.createEvent(gogEvent.event, BIRTHDAY_CALENDAR)
        if isinstance(newGoogleEvent, GoogleEvent):
            NotionUtils.updateBirthdayGoogleId(birth.id, newGoogleEvent.id)