'''
    INFO 1501 - Python I
    Welcome to the Health and Wellness System
    You will be working on this throughout the course and adding to it

    Please read instructions for each assignment clearly and don't go beyond the functionality
    required as we will be adding more each week.

    Make sure to merge branches and create new branches for each week's assignment.
'''

# This is the UI for the Health and Wellness system

# global dictionaries for meal and workout
# keys are date - in string format - for now
mealTracker = {} # each value is the calorie count for the meal
workoutTracker = {} # each entry is the calorie count burned from the workout

def add_meal():
    pass

def add_workout():
    pass

def search_date():
    pass

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
        choice = int(input("Choose operation: "))
        while choice < 1 or choice > 4:
            print("Invalid operation. Please choose a number from 1 to 4.")
            choice = int(input("Choose operation: "))

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


if __name__ == "__main__":
    main()