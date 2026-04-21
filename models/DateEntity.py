from datetime import date
from models.CalorieEntities import Meal
from models.CalorieEntities import Workout

class Day:
    def __init__(self, day : date): # create day object
        self.__day = day
        self.__meals = [] # create empty list for meals
        self.__workouts = [] # create empty list for workouts

    @property
    def day(self): # get the day/date property
        return self.__day
    @day.setter
    def day(self, value : date): # set the day/date property
        self.__day = value

    @property
    def meals(self) -> list: # get meals property
        return self.__meals
    @meals.setter
    def meals(self, value : list): # set meals property
        self.__meals = value

    @property
    def workouts(self) -> list:  # get meals property
        return self.__workouts
    @workouts.setter
    def workouts(self, value: list): # set meals property
        self.__workouts = value

    def add_meal(self, meal : Meal):
        # add Meal object to meals list
        self.__meals.append(meal)

    def add_workout(self, workout : Workout):
        # add Workout object to workouts list
        self.__workouts.append(workout)

    def meal_calories(self):
        # use list comprehension to add up total calories consumed for the day
        return sum([meal.calories for meal in self.meals])
        #total_calories = 0
        #for meal in self.meals:
        #    total_calories += meal.calories
        #return total_calories

    def workout_calories(self):
        # add up total calories burned for the day
        return sum([workout.calories for workout in self.workouts])
        #total_calories = 0
        #for workout in self.workouts:
        #    total_calories += workout.calories
        #return total_calories

    def net_calories(self) -> int :
        # subtract workout calories from meal calories, return net calories
        net_calories = self.meal_calories() - self.workout_calories()
        return net_calories

    def __eq__(self, other):
        return self.__day == other.day

    def __str__(self):
        # print out date, meals, and workouts
        return f"Date: {self.day}\nMeals: {self.meals_to_string()}\nWorkouts: {self.workouts_to_string()}\n"\
        f"\nNet Calories: {self.net_calories()}"

    def meals_to_string(self):
        # create string of meals
        string = ""
        for meal in self.meals:
            string += "\n\t" + str(meal)
        return string

    def workouts_to_string(self):
        # create string of workouts
        string = ""
        for workout in self.workouts:
            string += "\n\t" + str(workout)
        return string