from datetime import datetime, date

class Birthday:
    def __init__(self, name, date) -> None:
        self._name = name
        self._date = date

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