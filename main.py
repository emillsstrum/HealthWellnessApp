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

# global dictionaries for meal and workout
# keys are date - in string format - for now

from utils.input_util import *

mealTracker = {} # each value is the calorie count for the meal
workoutTracker = {} # each entry is the calorie count burned from the workout

def add_meal():
    print("## Add Meal Entry ##")
    date = prompt_date("Enter date of meal(MM/DD/YYYY): ")
    meal_details = input("Enter meal details: ")
    calories_consumed = prompt_int("Enter calories: ")

    # add to dictionary
    mealTracker[date] = {"meal_details":meal_details, "calorie_count":calories_consumed}

def add_workout():
    print("## Add Workout Entry##")
    date = prompt_date("Enter date of workout(MM/DD/YYYY): ")
    workout_details = input("Enter workout details: ")
    calories_burned = prompt_int("Enter calories burned: ")

    # add to dictionary
    workoutTracker[date] = {"workout_details":workout_details, "calories_burned":calories_burned}

def search_date():
    print("## Search for Entry ##")
    date = prompt_date("Enter date to search(MM/DD/YYYY): ")
    print() # blank space

    calories_consumed = 0
    calories_burned = 0
    if date in mealTracker:
        print("Meals:")
        print("Meal Items:", mealTracker[date]["meal_details"])
        print("Meal Calories:", mealTracker[date]["calorie_count"])
        calories_consumed = mealTracker[date]["calorie_count"]
    else:
        print("Meal: None")

    if date in workoutTracker:
        print("Workout:")
        print("Details:", workoutTracker[date]["workout_details"])
        print("Calories Burned:", workoutTracker[date]["calories_burned"])
        calories_burned = workoutTracker[date]["calories_burned"]
    else:
        print("Workout: None")
    pos = ""
    calorie_difference = calories_consumed - calories_burned
    if calorie_difference > 0:
        pos = "+"
    print() # blank space
    print("Calorie Difference:", pos + str(calorie_difference))

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
        while choice < 1 or choice > 4:
            print("Invalid operation. Please choose a number from 1 to 4.")
            choice = int(input("Choose operation: "))

        print() # blank space

        # call other functions based on input - You need to do this
        if choice == 1:
            add_meal()
        elif choice == 2:
            add_workout()
        elif choice == 3:
            search_date()
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
        print("Error, invalid input.")

def prompt_int_range(prompt, low, high):
    # convert string value to int
    # prompt user until valid input within range entered
    while True:
        str_value = input(prompt)
        value = get_int_range(str_value, low, high)
        if value:
            return value
        print("Error, input is out of range.")

def prompt_date(prompt):
    # prompt user until valid date in MM/DD/YYYY format entered
    while True:
        date_str = input(prompt)
        date = get_date(date_str)
        if date:
            return date
        print("Error, invalid date input.")

if __name__ == "__main__":
    main()