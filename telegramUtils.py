import requests
import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_APIKEY")
TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}'
TELEGRAM_MAINCHAT = os.getenv("TELEGRAM_MAINCHAT")

class TelegramUtils:
    def getMe():
        search_response = requests.post(
            TELEGRAM_URL + '/getMe')
        return search_response.json()
    
    def sendMessage(message):
        sendMessageUrl = f'{TELEGRAM_URL}/sendMessage?chat_id={TELEGRAM_MAINCHAT}&text={message}&parse_mode=HTML'
        search_response = requests.post(
            sendMessageUrl)
        return search_response.json()
    
    def getUpdates():
        getUpdateUrl = f'{TELEGRAM_URL}/getUpdates'
        response = requests.post(
            getUpdateUrl)
        return response.json()
