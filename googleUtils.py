import json

TIMEZONE_DEFAULT = 'Europe/Madrid'
EVENT_GOOGLEOBJECT = 'calendar#event'

class GoogleEvent:

    def __init__(self, eventObject={}) -> None:
        if 'id' in eventObject:
            self._id = eventObject["id"]
        if 'etag' in eventObject:
            self._etag = eventObject["etag"]
        if 'status' in eventObject:
            self._status = eventObject["status"]
        if 'htmlLink' in eventObject:
            self._htmlLink = eventObject["htmlLink"]
        if 'creator' in eventObject:
            self._creator = eventObject["creator"]
        if 'organizer' in eventObject:
            self._organizer = eventObject["organizer"]
        if 'extendedProperties' in eventObject:
            self._extendedProperties = eventObject["extendedProperties"]
        if 'created' in eventObject:
            self._createdAt = eventObject["created"]
        if 'updated' in eventObject:
            self._updatedAt = eventObject["updated"]
        if 'summary' in eventObject:
            self._summary = eventObject["summary"]
        if 'description' in eventObject:
            self._description = eventObject["description"]
        if 'start' in eventObject:
            self._start = eventObject["start"]
        if 'end' in eventObject:
            self._end = eventObject["end"]
        if 'iCalUID' in eventObject:
            self._iCalUID = eventObject["iCalUID"]
        if 'sequence' in eventObject:
            self._sequence = eventObject["sequence"]
        if 'reminders' in eventObject:
            self._reminders = eventObject["reminders"]
        if 'eventType' in eventObject:
            self._eventType = eventObject["eventType"]
        
    @property
    def event(self):
        googleEvent = {}
        if '_etag' in self.__dict__:
            googleEvent['etag'] = self._etag
        if '_summary' in self.__dict__:
            googleEvent['summary'] = self._summary
        if '_id' in self.__dict__:
            googleEvent['id'] = self._id
        if '_status' in self.__dict__:
            googleEvent['status'] = self._status
        if '_htmlLink' in self.__dict__:
            googleEvent['htmlLink'] = self._htmlLink
        if '_creator' in self.__dict__:
            googleEvent['creator'] = self._creator
        if '_organizer' in self.__dict__:
            googleEvent['organizer'] = self._organizer
        if '_extendedProperties' in self.__dict__:
            googleEvent['extendedProperties'] = self.extendedProperties
        if '_createdAt' in self.__dict__:
            googleEvent['created'] = self._createdAt
        if '_updatedAt' in self.__dict__:
            googleEvent['updated'] = self._updatedAt
        if '_description' in self.__dict__:
            googleEvent['description'] = self._description
        if '_start' in self.__dict__:
            googleEvent['start'] = self._start
        if '_end' in self.__dict__:
            googleEvent['end'] = self._end
        if '_iCalUID' in self.__dict__:
            googleEvent['iCalUID'] = self._iCalUID
        if '_sequence' in self.__dict__:
            googleEvent['sequence'] = self._sequence
        if '_reminders' in self.__dict__:
            googleEvent['reminders'] = self._reminders
        if '_eventType' in self.__dict__:
            googleEvent['eventType'] = self._eventType
        return googleEvent

    @property
    def id(self):
        return self._id
    
    @property
    def extendedProperties(self):
        return self._extendedProperties
    
    @extendedProperties.setter
    def extendedProperties(self, customProps):
        self._extendedProperties = customProps

    @property
    def creator(self):
        return self._creator
    
    @property
    def organizer(self):
        return self._organizer
    
    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self, startDate):
        self._start = startDate

    @property
    def end(self):
        return self._end
    
    @end.setter
    def end(self, endDate):
        self._end = endDate

    @property
    def summary(self):
        return self._summary
    
    @summary.setter
    def summary(self, name):
        self._summary = name

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def reminders(self):
        return self._reminders
    
    @reminders.setter
    def reminders(self, reminders):
        self._reminders = reminders

class GoogleError:
    def __init__(self, error=None) -> None:
        if error is not None:
            self._error = str(error)
            self._message = json.loads(error.content)['error']['errors'][0]['message']
            self._reason = error.reason
        
    @property
    def reason(self):
        return self._reason
    
    @reason.setter
    def reason(self, newReason):
        self._reason = newReason

    def notifyToAdmin(self):
        pass
