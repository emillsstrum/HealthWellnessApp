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
import services.health_data as db

def add_meal():
    # get date and meal data
    print("## Add Meal Entry ##")
    meal_date = prompt_date("Enter date of meal(MM/DD/YYYY): ")
    items = input("Enter meal details: ")
    calories = prompt_int("Enter calories: ")

    # add input to dictionary if date does not already exist in dictionary
    if db.add_meal(meal_date, {"items":items, "calories":calories}):
        print("* Entry added.")
    else:
        print("Error, date entry already added, try modifying entry.")

def add_workout():
    # get date and workout data
    print("## Add Workout Entry##")
    workout_date = prompt_date("Enter date of workout(MM/DD/YYYY): ")
    details = input("Enter workout details: ")
    calories = prompt_int("Enter calories burned: ")

    # add input to dictionary if date does not already exist in dictionary
    if db.add_workout(workout_date, {"details":details, "calories":calories}):
        print("* Entry added.")
    else:
        print("Error, date entry already added, try modifying entry.")

def search_entry():
    # get date input and output meal & workout data
    print("## Search for Entry ##")
    search_date = prompt_date("Enter date to search(MM/DD/YYYY): ")
    print() # blank space

    meal = db.get_meal(search_date)
    workout = db.get_workout(search_date)
    calories_consumed = 0
    calories_burned = 0
    if meal:
        # if dictionary entry exists, output the data
        calories_consumed = meal["calories"]
        print("Meals:")
        print("Meal Items:", meal["items"])
        print("Meal Calories:", calories_consumed)
    else:
        print("Meal: None")

    if workout:
        # if dictionary entry exists, output the data
        calories_burned = workout["calories"]
        print("Workout:")
        print("Details:", workout["details"])
        print("Calories Burned:", calories_burned)
    else:
        print("Workout: None")
    pos = ""
    # calculate calorie difference
    calorie_difference = calories_consumed - calories_burned
    if calorie_difference > 0:
        # if calorie difference > 0, add "+" to output
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