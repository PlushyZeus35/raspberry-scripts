from datetime import datetime, date

class Birthday:
    def __init__(self, name, date, googleId, notionId) -> None:
        self._name = name
        self._date = date
        self._gId = googleId
        self._nId = notionId

    @property
    def id(self):
        return self._nId

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nuevo_nombre):
        self._name = nuevo_nombre

    @property
    def date(self):
        return self._date
    
    @property
    def isToday(self):
        actualDate = date.today()
        birthDate = date(actualDate.year, self._date.date().month, self._date.date().day)
        return actualDate == birthDate

    @property
    def age(self):
        actualYear = date.today().year
        birthYear = self._date.year
        return actualYear - birthYear
    
    @property
    def actualDate(self):
        actualDate = date.today()
        return date(actualDate.year, self._date.date().month, self._date.date().day)
    
    @property
    def googleId(self):
        return self._gId
    @googleId.setter
    def googleId(self, googleId):
        self._gId = googleId