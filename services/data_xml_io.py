import xml.etree.ElementTree as ET

from models.SleepEntity import SleepSession, SleepQuality
from services.health_database import add_meal_to_database, add_workout_to_database
from utils.input_util import get_date, get_datetime
#from services.health_data import *
from models.CalorieEntities import *
from models.EntryType import *
import services.health_database as db

def read_in_xml(filename:str) :
    tree = ET.parse(filename)
    root = tree.getroot()

    for meal in root.findall("meal"): # loop through all the meal elements
        # get date attribute of meal element
        meal_date = get_date(meal.get("date"))

        # if date not in health_data, add it in
        #if get_entry(meal_date) is None:
        #    add_day(meal_date)

        # get the rest of the meal data
        description = meal.find("description").text
        calories = int(meal.find("calories").text)
        meal_type = MealType(meal.find("meal_type").text)

        # create Meal object
        new_meal = Meal(description, calories, meal_type)
        # add Meal to health_data
        #add_meal(meal_date, new_meal)

        # add meal to database
        db.add_meal_to_database(meal_date, new_meal)

    for workout in root.findall("workout"): # loop through all the workout elements
        # get date attribute of workout element
        workout_date = get_date(workout.get("date"))

        # get the rest of the sleep data

        description = workout.find("description").text
        calories = int(workout.find("calories").text)
        workout_type = WorkoutType(workout.find("workout_type").text)

        # create Workout object
        new_workout = Workout(description, calories, workout_type)
        # add Workout to health_data
        #add_workout(workout_date, new_workout)

        # add workout to database
        db.add_workout_to_database(workout_date, new_workout)

    for sleep in root.findall("sleep"): # loop through all the sleep elements
        # get date attribute of sleep element
        sleep_date = get_date(sleep.get("date"))

        # get the rest of the workout data
        start_time = get_datetime(sleep.find("start_time").text)
        end_time = get_datetime(sleep.find("end_time").text)
        quality = SleepQuality(int(sleep.find("sleep_quality").text))
        notes = sleep.find("notes").text

        # create Sleep Session object
        new_sleep_session = SleepSession(start_time, end_time, quality, notes)

        # add sleep session to database
        db.add_sleep_session_to_database(sleep_date, new_sleep_session)