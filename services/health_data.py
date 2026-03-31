from models.DateEntity import Day
from models.CalorieEntities import Meal
from models.CalorieEntities import Workout
from datetime import date

health_data = {} # dictionary to hold date/meal/workout data

def add_meal(date_input : date, meal : Meal):
    # if date (key) is in health_data, use to get Day object (value) in health_data
    # call add_meal() method of Day object (appends Meal object to meals list)
    if date_input in health_data:
        health_data[date_input].add_meal(meal)
        return True
    return False

def add_workout(date_input : date, workout : Workout):
    # if date (key) is in health_data, use to get Day object (value) in health_data
    # call add_workout() method of Day object (appends Workout object to workouts list)
    if date_input in health_data:
        health_data[date_input].add_workout(workout)
        return True
    return False

#def get_meal(date):
    # if date exists in mealTracker return meal data
    #if date in mealTracker:
    #    return mealTracker.get(date)
    #return None

#def get_workout(date):
    # if date exists in workoutTracker return workout data
    #if date in workoutTracker:
    #    return workoutTracker.get(date)
    #return None

def get_entry(date_input : date):
    # if date exists in health_data, return Day object
    if date_input in health_data:
        return health_data[date_input]
    return None

def add_day(date_input : date):
    # if date/day don't already exist in health_data, create Day object and add it to health_data
    if date_input not in health_data:
        health_data[date_input] = Day(date_input)
        return True
    return False
