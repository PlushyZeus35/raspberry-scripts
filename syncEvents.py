from googleUtils import GoogleEvent
from googleHelper import GoogleHelper

newEvent = GoogleEvent()
newEvent.summary = 'Test event name!!'
newEvent.description = 'This is a test event!!'
newEvent.start = {
    'date': '2023-11-24',
    'timeZone': 'America/Los_Angeles',
}
newEvent.end = {
    'date': '2023-11-24',
    'timeZone': 'America/Los_Angeles',
}
newEvent.extendedProperties = {
    "private": {
        "notionId": "asdffdsa1234"
    }
}
myId = '09q4dcp03rg7r2elubq8fpc54g'
birthCalendar = '963f9f32449806b9e2227be46a906f3d68b0aae9898d35e93909012d96298751@group.calendar.google.com'
googleHelper = GoogleHelper()
newGoogleEvent = googleHelper.getEvent('nkgijedfjvctdotjao1cgmqk0c', birthCalendar)
#evento = googleHelper.getEvent(myId)
print(newGoogleEvent.event)