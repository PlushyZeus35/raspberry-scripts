from mealPlanner import MealPlanner
from notionHelper import NotionUtils
SCRIPTNAME = 'Meal Planner'
meals = NotionUtils.getMealList()
plans = NotionUtils.getMealPlan()
planDictionary = {}
for plan in plans:
    planDictionary[plan.day] = plan

planner = MealPlanner(meals)
planner.makePlan()

for day in planner.planNotionFormat:
    targetPlan = planDictionary[day]
    targetPlan.meals = planner.planNotionFormat[day]
    NotionUtils.setMeals(targetPlan.id, targetPlan.meals)
NotionUtils.createLog(name=SCRIPTNAME, tags=['cron'])
