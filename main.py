'''
    INFO 1501 - Python I
    Welcome to the Health and Wellness System
    You will be working on this throughout the course and adding to it

    Please read instructions for each assignment clearly and don't go beyond the functionality
    required as we will be adding more each week.

    Make sure to merge branches and create new branches for each week's assignment.
'''

# This is the UI for the Health and Wellness system

# Resources used: lectures, reading, W3Schools

from utils.input_util import *
import services.health_data as db
from models.DateEntity import Day
from models.CalorieEntities import Meal
from models.CalorieEntities import Workout
from datetime import date

def add_meal():
    print("## Add Meal Entry ##")
    # get date input
    meal_date = prompt_date("Enter date of meal(MM/DD/YYYY): ")
    # if date doesn't exist in health_data dictionary, call add_day() to add it
    if db.get_entry(meal_date) is None:
        db.add_day(meal_date)
    # get meal details and calorie amount input
    items = input("Enter meal details: ")
    calories = prompt_int("Enter calories: ")
    #create Meal object
    meal = Meal(items, calories)
    # call health_data.py add_meal() to adds Meal to Day object
    if db.add_meal(meal_date, meal):
        print("* Entry added.")
    else: # if db.add_meal() returns false, print error message
        print("* Error, entry not added. Try modifying entry.")

def add_workout():
    print("## Add Workout Entry ##")
    # get date input
    workout_date = prompt_date("Enter date of workout(MM/DD/YYYY): ")
    # if date doesn't exist in health_data dictionary, call add_day() to add it
    if db.get_entry(workout_date) is None:
        db.add_day(workout_date)
    # get workout details and calorie amount
    details = input("Enter workout details: ")
    calories = prompt_int("Enter calories burned: ")
    # create Workout object
    workout = Workout(details, calories)
    # call health_data.py add_meal() to adds Meal to Day object
    if db.add_workout(workout_date, workout):
        print("* Entry added.")
    else: # if db.add_workout() returns false, print error message
        print("* Error, entry not added. Try modifying entry.")

def search_entry():
    # get date input to search for
    print("## Search for Entry ##")
    search_date = prompt_date("Enter date to search(MM/DD/YYYY): ")
    print() # blank space
    # if Day object exists in dictionary, print it
    entry = db.get_entry(search_date)
    if entry is not None:
        print(entry)
    else:
        print("* Error, entry not found")

def main():
    choice = 0
    while choice != 4:
        # print menu - We will be adding to these as we go throughout the course
        print("### Health and Wellness App ###")
        print("1. Add Meal")
        print("2. Add Workout")
        print("3. Search Date")
        print("4. Exit")

        # get input
        choice = prompt_int_range("Choose operation: ", 1, 4)

        print() # blank space

        # call other functions based on input - You need to do this
        if choice == 1:
            add_meal()
        elif choice == 2:
            add_workout()
        elif choice == 3:
            search_entry()
        elif choice == 4:
            print("System Exiting...")

        print() # blank space

# prompt functions
def prompt_int(prompt):
    # convert string value to int
    # prompt user until valid input entered
    while True:
        str_value = input(prompt)
        value = get_int(str_value)
        if value:
            return value
        print("Error, enter a valid number.")

def prompt_int_range(prompt, low, high):
    # convert string value to int
    # prompt user until valid input within range entered
    while True:
        str_value = input(prompt)
        value = get_int_range(str_value, low, high)
        if value:
            return value
        print("Error, enter a number within the range.")

def prompt_date(prompt):
    # prompt user until valid date in MM/DD/YYYY format entered
    while True:
        date_str = input(prompt)
        date = get_date(date_str)
        if date:
            return date
        print("Error, enter a valid date.")

if __name__ == "__main__":
    main()