'''
    INFO 1501 - Python I
    Welcome to the Health and Wellness System
    You will be working on this throughout the course and adding to it

    Please read instructions for each assignment clearly and don't go beyond the functionality
    required as we will be adding more each week.

    Make sure to merge branches and create new branches for each week's assignment.
'''
# This is the UI for the Health and Wellness system

# Resources used: lectures, reading, copilot AI to generate code for test data

from models.EntryType import MealType, WorkoutType
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
    # get meal type, meal details, and calorie amount input
    items = input("Enter meal details: ")
    calories = prompt_int("Enter calories: ")
    meal_type = get_meal_type()
    #create Meal object
    meal = Meal(items, calories, meal_type)
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
    # get workout type, workout details, and calorie amount
    details = input("Enter workout details: ")
    calories = prompt_int("Enter calories burned: ")
    workout_type = get_workout_type()
    # create Workout object
    workout = Workout(details, calories, workout_type)
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

def modify_meal():
    print("## Modify Meal ##")
    meals_list = search_meals("modify")
    # if no entry found for date or no meals found for entry, exit to main menu
    if meals_list is None:
        print("Exiting Modify Meal...")
        return

    # variables for list of meals and length of list
    meals_list_len = len(meals_list)
    choice = 0

    # loop through menu listing meals to modify
    while choice != (meals_list_len + 1):
        # print list of meals for searched date
        print()
        print("# Meal List #")
        for i in range(len(meals_list)):
            print(f"{i+1}. {meals_list[i]}")
        print(f"{meals_list_len+1}. Exit Meal Modification") # menu option to exit meal modification
        # get input for which meal to modify
        print()
        choice = prompt_int_range(f"Meal to modify (or enter {meals_list_len+1} to exit): ",
                                       1, (meals_list_len+1))

        # exit if user chooses to exit meal modification
        if choice == meals_list_len+1:
            print("Exiting Modify Meal...")
            return
        # otherwise send meal choice to modify attribute function
        meal_choice = meals_list[choice-1]
        modify_meal_attribute(meal_choice)

def modify_meal_attribute(current_meal):
    # print meal data and
    print()
    print("# Current Meal #")
    print(current_meal)

    # print options for updating meal data
    choice = 0
    while choice != 4:
        print()
        print("1. Modify Item Description")
        print("2. Modify Calories")
        print("3. Modify Meal Type")
        print("4. Exit Current Meal Modification")

        # get input for what attribute to modify
        mod_choice = prompt_int_range("Modify Attribute: ", 1, 4)

        # modify based on user input
        if mod_choice == 1:
            new_details = input("Enter new item details: ")
            current_meal.description = new_details
        if mod_choice == 2:
            new_calories = prompt_int("Enter new calories: ")
            current_meal.calories = new_calories
        if mod_choice == 3:
            new_meal_type = get_meal_type()
            current_meal.meal_type = new_meal_type
        if mod_choice == 4:
            print("Exiting current meal...")
            return
        print()
        print("# Current Meal #")
        print(current_meal)

def delete_meal():
    # get date and look up Day
    print("## Delete Meal ##")
    meals_list = search_meals("delete")

    # variable for length of list
    meals_list_len = len(meals_list)

    # print list of meals for searched date
    print()
    print("# Meal List #")
    for i in range(len(meals_list)):
        print(f"{i+1}. {meals_list[i]}")
    print(f"{meals_list_len+1}. Exit Meal Delete") # menu option to exit to main menu
    # get input for which meal to delete
    print()
    choice = prompt_int_range(f"Meal to delete (or enter {meals_list_len+1} to exit): ",
                                   1, (meals_list_len+1))

    # exit if user chooses to exit meal modification
    if choice == meals_list_len+1:
        return
    # otherwise delete meal selected by user
    meals_list.pop(choice-1)
    # print updated meal list
    print()
    print("# Meal List #")
    for i in range(len(meals_list)):
        print(f"{i + 1}. {meals_list[i]}")
    print("Exiting Delete Meal...")


def main():
    db.load_test_data()

    choice = 0
    while choice != 8:
        # print menu - We will be adding to these as we go throughout the course
        print("### Health and Wellness App ###")
        print("1. Add Meal")
        print("2. Add Workout")
        print("3. Search Date")
        print("4. Modify Meal")
        print("5. Delete Meal")
        print("6. Modify Workout")
        print("7. Delete Workout")
        print("8. Exit")

        # get input
        choice = prompt_int_range("Choose operation: ", 1, 8)

        print() # blank space

        # call other functions based on input - You need to do this
        if choice == 1:
            add_meal()
        elif choice == 2:
            add_workout()
        elif choice == 3:
            search_entry()
        elif choice == 4:
            modify_meal()
        elif choice == 5:
            delete_meal()
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            print("System Exiting...")

        print() # blank space

# helper functions
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

def get_meal_type():
    # print list of meal types, get user input for meal type
    print("Choose meal type: ")
    for index, meal_type in enumerate(MealType, start=1): # print options
        print(f"{index}. {meal_type}")

    choice = prompt_int_range("Enter your choice (1-" + str(len(MealType)) + "): ", 1, len(MealType))
    return list(MealType)[choice - 1] # return meal type chosen by user

def get_workout_type():
    # print list of meal types, get user input for workout type
    print("Choose workout type: ")
    for index, workout_type in enumerate(WorkoutType, start=1): # print options
        print(f"{index}. {workout_type}")

    choice = prompt_int_range("Enter your choice (1-" + str(len(WorkoutType)) + "): ", 1, len(WorkoutType))
    return list(WorkoutType)[choice - 1] # return workout type chosen by user

def search_meals(operation):
    # search date to find meals to modify or delete
    # prompt for date to look up Day
    search_date = prompt_date(f"Enter date to {operation}(MM/DD/YYYY): ")
    current = db.get_entry(search_date)

    if not current:
        # if get_entry returns None, date doesn't exist in collection, print message and exit
        print("No entry found for this date")
        return None
    elif len(current.meals) == 0:
        # if no meals listed for date, print message and exit
        print("No meals found for this date")
        return None
    # else return list of meals
    return current.meals

def search_workouts(operation):
    # search date to find workouts to modify or delete
    search_date = prompt_date(f"Enter date to {operation}(MM/DD/YYYY): ")
    current = db.get_entry(search_date)

    if not current:
        # if get_entry returns None, date doesn't exist in collection, print message and exit
        print("No entry found for this date")
        return None
    elif len(current.workouts) == 0:
        # if no workouts listed for date, print message and exit
        print("No meals found for this date")
        return None
    # else return list of workouts
    return current.workouts

if __name__ == "__main__":
    main()