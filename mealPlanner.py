import random

class Meal:
    def __init__(self, mealId, name):
        self._name = name
        self._id = mealId

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nuevo_nombre):
        self._name = nuevo_nombre
    
    @property
    def id(self):
        return self._id

class MealPlanner:
    def __init__(self, mealList):
        self._mealList = mealList

    @property
    def meals(self):
        return self._mealList

    @meals.setter
    def meals(self, mealList):
        self._mealList = mealList
    
    @property
    def plan(self):
        return self._mealPlan
    
    def makePlan(self):
        self._mealPlan = {'Lunes': [], 'Martes': [], 'Miércoles': [], 'Jueves': [], 'Viernes': [], 'Sábado': [], 'Domingo': []}
        auxList = self._mealList.copy()
        random.shuffle(auxList)
        for day in self._mealPlan.keys():
            if(len(auxList)>0):
                meal = auxList.pop()
                self._mealPlan[day].append(meal)
            if(len(auxList)>0):
                meal = auxList.pop()
                self._mealPlan[day].append(meal)
    @property
    def planNotionFormat(self):
        notionFormatList = {}
        for day in self._mealPlan.keys():
            mealsNotionFormat = []
            meals = self._mealPlan[day]
            for meal in meals:
                mealsNotionFormat.append({"id": meal.id})
            notionFormatList[day] = mealsNotionFormat
        return notionFormatList

class MealPlan:
    def __init__(self, mealPlanId, day, mealList):
        self._id = mealPlanId
        self._day = day
        self._mealList = mealList

    @property
    def id(self):
        return self._id
    
    @property
    def day(self):
        return self._day
    
    @property
    def meals(self):
        return self._mealList

    @meals.setter
    def meals(self, meals):
        self._mealList = meals


    