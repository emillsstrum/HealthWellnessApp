import xml.etree.ElementTree as ET
from utils.input_util import get_date
from services.health_data import *
from models.EntryType import *

def read_in_xml(filename:str) :
    tree = ET.parse(filename)
    root = tree.getroot()

    for meal in root.findall("meal"): # loop through all the meal elements
        # get date attribute of meal element
        meal_date = get_date(meal.get("date"))

        # if date not in health_data, add it in
        if get_entry(meal_date) is None:
            add_day(meal_date)

        # get the rest of the meal data
        description = meal.find("description").text
        calories = int(meal.find("calories").text)
        meal_type = MealType(meal.find("meal_type").text)

        # create Meal object
        new_meal = Meal(description, calories, meal_type)
        # add Meal to health_data
        add_meal(meal_date, new_meal)

    for workout in root.findall("workout"): # loop through all the workout elements
        # get date attribute of workout element
        workout_date = get_date(workout.get("date"))

        # if date not in health_data, add it in
        if get_entry(workout_date) is None:
            add_day(workout_date)

        # get the rest of the workout data
        description = workout.find("description").text
        calories = int(workout.find("calories").text)
        workout_type = WorkoutType(workout.find("workout_type").text)

        # create Workout object
        new_workout = Workout(description, calories, workout_type)
        # add Workout to health_data
        add_workout(workout_date, new_workout)