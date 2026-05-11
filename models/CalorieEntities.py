from models.HealthEntry import HealthEntry
from models.EntryType import MealType, WorkoutType

class Meal(HealthEntry):
    def __init__(self, description, calories, meal_type:MealType, meal_id=0): # create Meal object
        super().__init__(description, calories, meal_id)
        self.meal_type = meal_type

    # getter and setter for meal_type
    @property
    def meal_type(self):
        return self.__meal_type
    @meal_type.setter
    def meal_type(self, value):
        if isinstance(value, MealType): # check if value is Enum type
            self.__meal_type = value
        else: # if not, set as default (Snack)
            self.__meal_type = MealType.SNACK

    def __str__(self): # override super class __str__ method
        return f"Meal: {self.description}, Calories Consumed: {self.calories}, Meal Type: {self.meal_type}"

    def to_dict(self) -> dict: # create dictionary for object
        return {"description": self.description, "calories": self.calories, "meal_type": str(self.meal_type)}


class Workout(HealthEntry):
    def __init__(self, description, calories, workout_type:WorkoutType, wo_id=0): # create Workout object
        super().__init__(description, calories, wo_id)
        self.workout_type = workout_type

    # getter and setter for workout_type
    @property
    def workout_type(self):
        return self.__workout_type
    @workout_type.setter
    def workout_type(self, value):
        if isinstance(value, WorkoutType): # check if value is Enum type
            self.__workout_type = value
        else: # if not, set as default (Other)
            self.__workout_type = WorkoutType.OTHER

    def __str__(self): # override super class __str__ method
        return f"Workout: {self.description}, Calories Burned: {self.calories}, Workout Type: {self.workout_type}"

    def to_dict(self) -> dict: # create dictionary for object
        return {"description": self.description, "calories": self.calories, "workout_type": str(self.workout_type)}