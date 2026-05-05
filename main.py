'''
    INFO 1501 - Python I
    Welcome to the Health and Wellness System
    You will be working on this throughout the course and adding to it

    Please read instructions for each assignment clearly and don't go beyond the functionality
    required as we will be adding more each week.

    Make sure to merge branches and create new branches for each week's assignment.
'''
# This is the UI for the Health and Wellness system

# Resources used: lectures, reading

from utils.input_util import *
#import services.health_data as db
from services.data_xml_io import read_in_xml
from services.data_json_io import *
from services.data_csv_report import write_out_report
import services.health_database as db

def add_meal():
    print("## Add Meal Entry ##")
    # get date input
    meal_date = prompt_date("Enter date of meal(MM/DD/YYYY): ")

    # if date doesn't exist in health_data dictionary, call add_day() to add it
    #if db.get_entry(meal_date) is None:
    #    db.add_day(meal_date)

    # get meal type, meal details, and calorie amount input
    items = input("Enter meal details: ")
    calories = prompt_int("Enter calories: ")
    meal_type = get_meal_type()

    #create Meal object
    meal = Meal(items, calories, meal_type)

    # add meal to database
    #if db.add_meal(meal_date, meal):
    if db.add_meal_to_database(meal_date, meal):
        print("* Entry added.")
    else: # print error message
        print("* Error, entry not added. Try modifying entry.")

def add_workout():
    print("## Add Workout Entry ##")
    # get date input
    workout_date = prompt_date("Enter date of workout(MM/DD/YYYY): ")

    # if date doesn't exist in health_data dictionary, call add_day() to add it
    #if db.get_entry(workout_date) is None:
    #    db.add_day(workout_date)

    # get workout type, workout details, and calorie amount
    details = input("Enter workout details: ")
    calories = prompt_int("Enter calories burned: ")
    workout_type = get_workout_type()

    # create Workout object
    workout = Workout(details, calories, workout_type)

    # add workout to database
    #if db.add_workout(workout_date, workout):
    if db.add_workout_to_database(workout_date, workout):
        print("* Entry added.")
    else: # print error message
        print("* Error, entry not added. Try modifying entry.")

def search_entry():
    # get date input to search for
    print("## Search for Entry ##")
    search_date = prompt_date("Enter date to search(MM/DD/YYYY): ")
    print() # blank space
    # if Day object exists in dictionary, print it
    #entry = db.get_entry(search_date)

    # get day object with meals and workouts that match date
    entry = db.get_day(search_date)

    # print results
    if entry is not None:
        print(entry)
    else:
        print("* Error, entry not found")

def print_list_entries(current_list:list, calorie_entity:str):
    # list out the meals or workouts
    print()
    print(f"{calorie_entity} List")
    for i in range (len(current_list)):
        print(f"{i+1}. {current_list[i]}")

def search_to_modify_or_delete():
    # search date to find meals to modify
    # prompt for date to look up Day
    search_date = prompt_date(f"Enter date to modify (MM/DD/YYYY): ")
    current = db.get_day(search_date)
    return current

def modify_attribute(calorie_entity:str):
    print(f"## Modify {calorie_entity} ## ")
    current = search_to_modify_or_delete()

    # if get_entry returns None, date doesn't exist in collection, print message and exit to main menu
    if not current:
        print("No entry found for this date")
        return

    # set variable for meal or workout list
    current_list = ""
    if calorie_entity == "Meal":
        current_list = current.meals
    elif calorie_entity == "Workout":
        current_list = current.workouts

    # print menu, get user choice
    choice = 0
    while choice != (len(current_list) + 1):
        # print entries
        print_list_entries(current_list, calorie_entity)
        # print exit option
        print(f"{len(current_list)+1}. Exit to main menu")

        # get user choice
        choice = prompt_int_range(f"{calorie_entity} to modify (or {len(current_list)+1} to exit): ",
                                  1, len(current_list)+1)
        # exit if user chooses to exit meal modification
        if choice == len(current_list)+1:
            print("Exiting Modify Meal...")
            return

        # otherwise modify attribute
        # set variable for user's meal/workout choice
        item_to_modify = current_list[choice-1]
        # print meal/workout data
        print()
        print(f"# Current {calorie_entity} #")
        print(current_list[choice-1])
        # print options for updating meal data
        mod_choice = 0
        while mod_choice != 4:
            print()
            print("1. Modify Item Description")
            print("2. Modify Calories")
            print(f"3. Modify {calorie_entity} Type")
            print(f"4. Exit Current {calorie_entity} Modification")
            # get input for what attribute to modify
            mod_choice = prompt_int_range("Modify Attribute: ", 1, 4)

            # modify based on user input
            if mod_choice == 1:
                new_details = input("Enter new item details: ")
                item_to_modify.description = new_details
            if mod_choice == 2:
                new_calories = prompt_int("Enter new calories: ")
                item_to_modify.calories = new_calories
            if mod_choice == 3:
                if calorie_entity == "Meal":
                    new_type = get_meal_type()
                    item_to_modify.meal_type = new_type
                elif calorie_entity == "Workout":
                    new_type = get_workout_type()
                    item_to_modify.workout_type = new_type
            if mod_choice == 4:
                print("Exiting...")
                return

            # print updated meal/workout data
            print()
            print(f"# Current {calorie_entity} #")
            print(current_list[choice - 1])

def delete_entry(calorie_entity:str):
    print(f"## Delete {calorie_entity} ## ")
    current = search_to_modify_or_delete()

    # if get_entry returns None, date doesn't exist in collection, print message and exit to main menu
    if not current:
        print("No entry found for this date")
        return

    # set variable for meal or workout list
    current_list = ""
    if calorie_entity == "Meal":
        current_list = current.meals
    elif calorie_entity == "Workout":
        current_list = current.workouts

    # print menu, get user choice
    choice = 0
    while choice != (len(current_list) + 1):
        # print entries
        print_list_entries(current_list, calorie_entity)
        # print exit option
        print(f"{len(current_list) + 1}. Exit to main menu")

        # get user choice
        choice = prompt_int_range(f"{calorie_entity} to delete (or {len(current_list) + 1} to exit): ",
                                  1, len(current_list) + 1)
        # exit if user chooses to exit meal modification
        if choice == len(current_list) + 1:
            print(f"Exiting Delete {calorie_entity}...")
            return

        # otherwise delete meal or workout
        current_list.pop(choice-1)

def filter_by_date():
    # print header
    print("## Filter by Date ##")
    print("1. Filter by Year")
    print(f"2. Filter by Month")
    print("3. Filter by Date Range")
    print("4. Exit to main menu")

    choice = prompt_int_range("Filter operation: ", 1, 4)

    if choice == 1:
        # filter by year
        print()
        # get year input and pass to filter function
        year = prompt_int("Enter year to filter: ")
        day_list = db.filter_by_year(year)
        # print list of entries found
        print(f"\n* Entries in {year}")
        if len(day_list) == 0:
            print(f"No entries found in {year}.")
            return
        for d in day_list:
            print("****************")
            print(d)
            print()
        # find and print sum of calories for entries found
        net_calorie_sum = sum([day.net_calories() for day in day_list])
        print(f"* Net calories for {year}: {net_calorie_sum}")
        # provide option to save out data as report
        save_report(day_list)
    elif choice == 2:
        # filter by month
        print()
        # get year input
        year = prompt_int("Enter year of month to filter: ")
        # get month input and pass to filter function
        month = prompt_int_range("Enter month to filter (1-12): ", 1, 12)
        day_list = db.filter_by_month(month, year)
        # print list of entries found
        print(f"\n* Entries in {list_of_months[month-1]}")
        if len(day_list) == 0:
            print(f"No entries found in {list_of_months[month-1]} {date.today().year}.")
            return
        for d in day_list:
            print("****************")
            print(d)
            print()
        # find and print sum of calories for entries found
        net_calorie_sum = sum([day.net_calories() for day in day_list])
        print(f"* Net calories for {list_of_months[month-1]}: {net_calorie_sum}")
        # provide option to save out data as report
        save_report(day_list)
    elif choice == 3:
        # filter by date range
        print()
        # get date range input and pass to filter function
        start_date = prompt_date("Enter start date (MM/DD/YYYY): ")
        end_date = prompt_date("Enter end date (MM/DD/YYYY): ")
        # while end date is not later than start date, prompt for input
        while end_date < start_date:
            print("Error, end date must come after start date")
            start_date = prompt_date("Enter start date: ")
            end_date = prompt_date("Enter end date: ")
        day_list = db.filter_by_date_range(start_date, end_date)
        # print list of entries found
        print(f"\n* Entries in range {start_date} to {end_date}")
        if len(day_list) == 0:
            print("No entries found in this date range.")
            return
        for d in day_list:
            print("****************")
            print(d)
            print()
        # find and print sum of calories for entries found
        net_calorie_sum = sum([day.net_calories() for day in day_list])
        print(f"* Net calories for this range: {net_calorie_sum}")
        # provide option to save out data as report
        save_report(day_list)
    elif choice == 4:
        print("Exiting Filter by Date...")
        return

def save_report(day_list):
    # print options to save data to report or exit
    print("# Save Report #")
    print("1. Save to CSV")
    print("2. Exit to main menu")
    choice = prompt_int_range("Choose option: ", 1, 2)

    if choice == 1:
        # get input for filename
        filename = input("Enter filename: ")
        if not filename.endswith(".csv"): # if filename doesn't end with .csv, add to end
            filename = filename + ".csv"
        # convert data to list of dictionaries
        report_list = [day.to_report() for day in day_list]
        # send list to write_out_report() to write data to csv file
        write_out_report(filename, report_list)
        print("\n* Saved to CSV")
    elif choice == 2:
        print("Exiting Filter by Date...")
        return

def load_xml():
    # make sure file exists before passing it to XML read function
    print("## Load XML File Data ##")
    # get filename
    filename = input("Enter XML file to load: ")

    # check if file exists
    if not os.path.exists(filename): # if it doesn't, print error message
        print("Error: File not found, no data loaded.")
        return
    read_in_xml(filename) # if file exists, pass it to XML read function
    print("File loaded successfully.")

def main():
    #db.load_test_data()
    #read_in_json() # read in data from JSON file

    EXIT = 10
    choice = 0
    while choice != EXIT:
        # print menu - We will be adding to these as we go throughout the course
        print("### Health and Wellness App ###")
        print("1. Add Meal")
        print("2. Add Workout")
        print("3. Search Date")
        print("4. Modify Meal")
        print("5. Delete Meal")
        print("6. Modify Workout")
        print("7. Delete Workout")
        print("8. Filter by Date")
        print("9. Load in from XML")
        print(str(EXIT) + ". Exit")

        # get input
        choice = prompt_int_range("Choose operation: ", 1, EXIT)

        print() # blank space

        # call other functions based on input - You need to do this
        if choice == 1:
            add_meal()
        elif choice == 2:
            add_workout()
        elif choice == 3:
            search_entry()
        elif choice == 4:
            modify_attribute("Meal") # modify meal
        elif choice == 5:
            delete_entry("Meal") # delete meal
        elif choice == 6:
            modify_attribute("Workout") # modify workout
        elif choice == 7:
            delete_entry("Workout") # delete workout
        elif choice == 8:
            filter_by_date()
        elif choice == 9:
            load_xml()
        else: # exit option
            print("System Exiting...")
            #write_out_json()  # write out data to JSON file
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

if __name__ == "__main__":
    main()