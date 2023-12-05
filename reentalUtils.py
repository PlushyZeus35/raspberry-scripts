from dotenv import load_dotenv
import os
import requests
load_dotenv()
EXCHANGE_APIKEY = os.getenv("EXCHANGERATES_APIKEY")
class ReentalToken():
    def __init__(self, name, tokenName, amount, currency, eurValue, dolValue, realValue, notionPage) -> None:
        self._name = name
        self._tokenName = tokenName
        self._amount = amount
        self._currency = currency
        self._eurValue = eurValue
        self._dolValue = dolValue
        self._realValue = realValue
        self._nId = notionPage

    @property
    def realValue(self):
        return self._realValue
    
    @property
    def eurValue(self):
        return self._eurValue
    
    @property
    def dolValue(self):
        return self._dolValue
    
    @property
    def notionId(self):
        return self._nId

    def updateRealValue(self):
        if self._currency == 'Euro':
            self._realValue = self._eurValue
        else:
            self._realValue = round(self._dolValue * self.getEurValue(), 4)
        return self._realValue
    
    def getEurValue(self):
        url = f'http://api.exchangeratesapi.io/v1/latest?access_key={EXCHANGE_APIKEY}&base=EUR&symbols=USD'
        search_response = requests.get(url)
        value = search_response.json()
        if value['success']==True:
            eurDol = value['rates']['USD']
            return 1.0 / eurDol
        return 1.00
