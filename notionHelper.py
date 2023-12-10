import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from mealPlanner import Meal, MealPlan
from birthdayUtils import Birthday
from reentalUtils import ReentalToken
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
MEALDB_ID = os.getenv("MEALS_NOTIONDB")
PLANDB_ID = os.getenv("MEALPLAN_NOTIONDB")
BITHDAY_ID = os.getenv("BITHDAY_NOTIONDB")
LOGDB_ID = os.getenv("LOG_NOTIONDB")
REENTALTOKEN_ID = os.getenv("REENTALTOKEN_NOTIONDB")
AUTOMATIONDB_ID = os.getenv("REENTALAUTOMATION_NOTIONDB")
TOKENDB_ID = os.getenv("REENTALTOKEN_NOTIONDB")
MEALQUERY_URL = f'https://api.notion.com/v1/databases/{MEALDB_ID}/query'
PLANQUERY_URL = f'https://api.notion.com/v1/databases/{PLANDB_ID}/query'
BIRTHDAYQUERY_URL = f'https://api.notion.com/v1/databases/{BITHDAY_ID}/query'
TOKENQUERY_URL = f'https://api.notion.com/v1/databases/{TOKENDB_ID}/query'
REENTALTOKENQUERY_URL = f'https://api.notion.com/v1/databases/{REENTALTOKEN_ID}/query'
AUTOMATION_URL = f'https://api.notion.com/v1/databases/{AUTOMATIONDB_ID}/query'
EDITPAGE_URL = f'https://api.notion.com/v1/pages/'
headers = {'Authorization': f"Bearer {NOTION_TOKEN}", 
           'Content-Type': 'application/json', 
           'Notion-Version': '2022-06-28'}

class NotionUtils:
    def getPage(pageId):
        search_params = {}
        search_response = requests.get(
            EDITPAGE_URL + pageId, 
            json = search_params, headers=headers)
        return search_response.json()
        
    def getMealList():
        mealList = []
        search_params = {}
        search_response = requests.post(
            MEALQUERY_URL, 
            json = search_params, headers=headers)
        result = search_response.json()['results']
        for meal in result:
            mealList.append(NotionUtils.notionToMeal(meal))
        return mealList

    def getMealPlan():
        search_params = {}
        mealPlans = []
        search_response = requests.post(
            PLANQUERY_URL, 
            json = search_params, headers=headers)
        for mealPlan in search_response.json()['results']:
            mealPlans.append(NotionUtils.notionToMealPlan(mealPlan))
        return mealPlans
    
    def notionToMeal(notionMeal) -> Meal:
        mealName = notionMeal['properties']['Nombre']['title'][0]['text']['content']
        mealId = notionMeal['id']
        return Meal(mealId, mealName)
    
    def notionToMealPlan(mealPlan) -> MealPlan:
        mealPlanId = mealPlan['id']
        mealPlanDay = mealPlan['properties']['Nombre']['title'][0]['text']['content']
        mealPlanMealList = mealPlan['properties']['Comidas']['relation']
        return MealPlan(mealPlanId, mealPlanDay, mealPlanMealList)
    
    def setMeals(dayId, meals):
        editUrl = EDITPAGE_URL + dayId
        search_params = {
            "properties": {
                "Comidas": { "relation": meals }
            }
        }
        search_response = requests.patch(
            editUrl, 
            json = search_params, headers=headers)
        return search_response.json()
    
    def getBirthdays():
        date_format = "%Y-%m-%d"
        search_params = {}
        births = []
        search_response = requests.post(
            BIRTHDAYQUERY_URL, 
            json = search_params, headers=headers)
        for birth in search_response.json()["results"]:
            name = birth["properties"]["Nombre"]["title"][0]["text"]["content"]
            date = birth["properties"]["Fecha"]["date"]["start"]
            googleId = birth["properties"]["googleId"]['rich_text']
            googleId = googleId[0]['text']['content'] if len(googleId)>0 else None
            pageId = birth["id"]
            births.append(Birthday(name, datetime.strptime(date, date_format), googleId, pageId))
        return births
    
    def updateBirthdayGoogleId(birthId, googleId):
        editUrl = EDITPAGE_URL + birthId
        search_params = {
            "properties": {
                "googleId": { "rich_text": [{'text': {'content': googleId}}] }
            }
        }
        search_response = requests.patch(
            editUrl, 
            json = search_params, headers=headers)
        return search_response.json()
    
    def getToken(service=''):
        search_params = {
            "filter": {
                "property": "Nombre",
                "title": {
                    "equals": service
                }
            }
        }
        search_response = requests.post(
            TOKENQUERY_URL, 
            json = search_params, headers=headers)
        results = search_response.json()['results']
        if(len(results)>0):
            returnToken = ""
            for tokenarr in results[0]['properties']['Token']['rich_text']:
                returnToken += tokenarr['text']['content']
            return returnToken
        else:
            return ''
        pass

    def createLog( name='', description='', amount=None, tags=[]):
        automationId = ''
        # Get automation id
        search_params = {
            "filter": {
                "property": "Nombre",
                "title": {
                    "equals": name
                }
            }
        }
        search_response = requests.post(
            AUTOMATION_URL, 
            json = search_params, headers=headers)
        results = search_response.json()['results']
        if len(results)>0:
            automationId = results[0]['id']
        print(automationId)
        notionTags = []
        for tag in tags:
            notionTags.append({"name": tag})
        search_params = {
            "parent": { "database_id": LOGDB_ID },
            "properties": {
                "Nombre": {
                    "title": [
                        {
                            "text": {
                                "content": name
                            }
                        }
                    ]
                },
                "Descripcion": {
                    "rich_text": [
                        {
                            "text": {
                                "content": description
                            }
                        }
                    ]
                },
                "Etiquetas": {"multi_select": notionTags},
                "Cantidad": { "number": amount }
            }
        }
        if automationId!='':
            search_params['properties']['Automatizaciones']={'relation': [{'id': automationId}]}
        search_response = requests.post(
            EDITPAGE_URL, 
            json = search_params, headers=headers)
        return search_response.json()
    
    def getReentalTokens():
        search_params = {}
        reentalTokens = []
        search_response = requests.post(
            REENTALTOKENQUERY_URL, 
            json = search_params, headers=headers)
        for token in search_response.json()['results']:
            nId = token['id']
            name = token['properties']['Nombre']['title'][0]['text']['content']
            tokenName = token['properties']['Token']['rich_text'][0]['text']['content']
            amount = token['properties']['Cantidad']['number']
            currency = token['properties']['Divisa']['select']['name']
            eurValue = token['properties']['Valor euros']['number']
            dolValue = token['properties']['Valor dólares']['number']
            finValue = token['properties']['Valor real']['number']
            reentalTokens.append(ReentalToken(name, tokenName, amount, currency, eurValue, dolValue, finValue, nId))
        return reentalTokens
    
    def updateReentalTokenFinalValue(notionId, finalValue):
        editUrl = EDITPAGE_URL + notionId
        search_params = {
            "properties": {
                "Valor real": { "number": finalValue }
            }
        }
        search_response = requests.patch(
            editUrl, 
            json = search_params, headers=headers)
        return search_response.json()