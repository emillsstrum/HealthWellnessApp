from models.HealthEntry import HealthEntry
from models.EntryType import MealType, WorkoutType

class Meal(HealthEntry):
    def __init__(self, description, calories, meal_type:MealType): # create Meal object
        super().__init__(description, calories)
        self.__meal_type = meal_type

    # getter and setter for meal_type
    @property
    def meal_type(self):
        return self.__meal_type
    @meal_type.setter
    def meal_type(self, value):
        self.__meal_type = value


    def __str__(self): # override super class __str__ method
        return f"Meal: {self.description}, Calories Consumed: {self.calories}, Meal Type: {self.meal_type}"

class Workout(HealthEntry):
    def __init__(self, description, calories, workout_type:WorkoutType): # create Workout object
        super().__init__(description, calories)
        self.__workout_type = workout_type

    # getter and setter for workout_type
    @property
    def workout_type(self):
        return self.__workout_type
    @workout_type.setter
    def workout_type(self, value):
        self.__workout_type = value

    def __str__(self): # override super class __str__ method
        return f"Workout: {self.description}, Calories Burned: {self.calories}, Workout Type: {self.workout_type}"
