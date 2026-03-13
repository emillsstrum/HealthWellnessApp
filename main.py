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

# TODO: Create functions to add meal, add workout and search via date in the dictionary.

def main():
    # TODO: You need to make this system file loop for the menu until they exit.
    # print menu - We will be adding to these as we go throughout the course
    print("### Health and Wellness App ###")
    print("1. Add Meal")
    print("2. Add Workout")
    print("3. Search Date")
    print("4. Exit")

    # get input
    choice = int(input("Choose operation: "))

    # TODO: You need to validate the choice operation input is between 1-4 using a while loop NOT just having else on the if/elif below.

    # call other functions based on input - You need to do this
    # TODO: You need to create other functions outside of main and call them here for each operation.
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("System Exitting...")


if __name__ == "__main__":
    main()