import requests
import os
from dotenv import load_dotenv
from mealPlanner import Meal, MealPlan
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
MEALDB_ID = os.getenv("MEALS_NOTIONDB")
PLANDB_ID = os.getenv("MEALPLAN_NOTIONDB")
MEALQUERY_URL = f'https://api.notion.com/v1/databases/{MEALDB_ID}/query'
PLANQUERY_URL = f'https://api.notion.com/v1/databases/{PLANDB_ID}/query'
EDITPAGE_URL = f'https://api.notion.com/v1/pages/'
headers = {'Authorization': f"Bearer {NOTION_TOKEN}", 
           'Content-Type': 'application/json', 
           'Notion-Version': '2022-06-28'}

class NotionUtils:
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
        # [{"id": EXAMPLEMEAL1},{"id": EXAMPLEMEAL2}]
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