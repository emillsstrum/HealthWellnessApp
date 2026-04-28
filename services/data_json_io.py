import json
import os
from services.health_data import *
from utils.input_util import get_date

def write_out_json():
    # get Day objects in health_data{}, convert to list of dictionaries, write to json file
    json_data = [day.to_dict() for day in health_data.values()] # get list of dictionaries

    with open("health_data.json", "w") as file: # write data to json file
        json.dump(json_data, file, indent=4)

def read_in_json():
    # check if file exists
    if not os.path.exists("health_data.json"):
        return

    with open("health_data.json", "r") as file: # read in data from JSON file
        json_data = json.load(file)

        for day in json_data: # loop through data
            day_date = get_date(day.get("date")) # get date and convert from string to date object

            # if date not in health_data, add it in
            if get_entry(day_date) is None:
                add_day(day_date)

            for meal in day.get("meals"): # loop through meals & get meal data
                description = meal.get("description")
                calories = meal.get("calories")
                meal_type = MealType(meal.get("meal_type"))

                # create Meal object
                new_meal = Meal(description, calories, meal_type)
                # add meal to health_data{}
                add_meal(day_date, new_meal)

            for workout in day.get("workouts"):  # loop through workouts & get workout data
                description = workout.get("description")
                calories = workout.get("calories")
                workout_type = WorkoutType(workout.get("workout_type"))

                # create Workout object
                new_workout = Workout(description, calories, workout_type)
                # add workout to health_data{}
                add_workout(day_date, new_workout)





