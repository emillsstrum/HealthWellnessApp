'''
    INFO 1501 - Python I
    Welcome to the Health and Wellness System
    You will be working on this throughout the course and adding to it

    Please read instructions for each assignment clearly and don't go beyond the functionality
    required as we will be adding more each week.

    Make sure to merge branches and create new branches for each week's assignment.
'''
from models.SleepEntity import SleepQuality, SleepSession
# This is the UI for the Health and Wellness system

# Resources used: lectures, reading

from utils.input_util import *
#import services.health_data as db
from services.data_xml_io import read_in_xml
from services.data_json_io import *
from services.data_csv_report import write_out_report
import services.health_database as db
from datetime import timedelta

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

def add_sleep():
    print("## Add Sleep Session ##")
    # get type of sleep
    choice = 0
    print("Type of Sleep:")
    print("1. Overnight")
    print("2. Same day sleep")
    choice = prompt_int_range("Enter type of sleep: ", 1, 2)

    # get date input
    sleep_date = prompt_date("\nEnter date of sleep session (date you woke up - MM/DD/YYYY): ")

    # get start time & wake-up time, make sure they're in correct order
    start_time = prompt_time("Enter start time(HH:MM): ")
    end_time = prompt_time("Enter wake up time(HH:MM): ")

    # combine time and date to make datetime objects
    if choice == 1:
        start_datetime = datetime.combine(sleep_date - timedelta(days=1), start_time)
    else:
        start_datetime = datetime.combine(sleep_date, start_time)
    end_datetime = datetime.combine(sleep_date, end_time)

    # make sure datetimes in correct order, exit if not
    if start_datetime > end_datetime:
        print("\n* Error, wake up must be after start time/date.")
        return

    # get sleep quality and notes
    quality = get_sleep_quality()
    notes = input("\nEnter notes on the sleep: ")

    # create Sleep Session object
    sleep = SleepSession(start_datetime, end_datetime, quality, notes)

    # add sleep session to database
    if db.add_sleep_session_to_database(sleep_date, sleep):
        print("* Sleep session added.")
    else:  # print error message
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
    print(f"# {calorie_entity} List #")
    for i in range (len(current_list)):
        print(f"{i+1}. {current_list[i]}")

def search_to_modify_or_delete():
    # search date to find meals/workouts to modify
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
            print("1. Modify Item Description")
            print("2. Modify Calories")
            print(f"3. Modify {calorie_entity} Type")
            print(f"4. Exit Current {calorie_entity} Modification")
            # get input for what attribute to modify
            mod_choice = prompt_int_range("Modify Attribute: ", 1, 4)
            print()

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
                # call update function on exit
                if calorie_entity == "Meal":
                    db.update_meal(item_to_modify)
                elif calorie_entity == "Workout":
                    db.update_workout(item_to_modify)
                print(f"Exiting Current {calorie_entity} Modification...")

            # print updated meal/workout data
            print()
            print(f"# Current {calorie_entity} #")
            print(current_list[choice - 1])

def modify_sleep_attribute():
    print("## Modify Sleep ##")
    # prompt for date to look up Day
    search_date = prompt_date(f"Enter date to modify (MM/DD/YYYY): ")
    current = db.get_day(search_date)

    # if get_entry returns None, date doesn't exist in collection, print message and exit to main menu
    if not current:
        print("No entry found for this date")
        return

    # set variable for list
    current_list = current.sleep_sessions

    # print menu, get user choice
    choice = 0
    while choice != (len(current_list) + 1):
        # print entries
        print_list_entries(current_list, "Sleep")
        # print exit option
        print(f"{len(current_list)+1}. Exit to main menu")

        # get user choice
        choice = prompt_int_range(f"Sleep to modify (or {len(current_list)+1} to exit): ",
                                  1, len(current_list)+1)
        # exit if user chooses to exit modification
        if choice == len(current_list)+1:
            print("Exiting Modify Sleep...")
            return

        # otherwise modify attribute
        # set variable for user's choice
        item_to_modify = current_list[choice-1]

        # print sleep session data
        print()
        print("# Current Sleep Session #")
        print(current_list[choice-1])

        # print options for updating sleep session data
        mod_choice = 0
        while mod_choice != 5:
            print("1. Modify Start Time")
            print("2. Modify End Time")
            print("3. Modify Quality")
            print("4. Modify Notes")
            print("5. Exit Current Sleep Modification")

            # get input for what attribute to modify
            mod_choice = prompt_int_range("Modify Attribute: ", 1, 5)
            print()

            # modify based on user input
            if mod_choice == 1: # modify start time
                # get type of sleep
                type_choice = 0
                print("Type of Sleep:")
                print("1. Overnight")
                print("2. Same day sleep")
                prompt_int_range("Enter type of sleep: ", 1, 2)

                # get new start time
                new_start_time = prompt_time("\nEnter new start time(HH:MM): ")

                # modify datetime variable based on type of sleep
                if type_choice == 1:
                    start_datetime = datetime.combine(current.day - timedelta(days=1), new_start_time)
                else:
                    start_datetime = datetime.combine(current.day, new_start_time)

                # make sure start time before end time
                if start_datetime < item_to_modify.end_time:
                    item_to_modify.start_time = start_datetime # modify start time
                else:
                    print("* Error, the start time needs to be before end time.")
                    #return
            elif mod_choice == 2: # modify end time
                # get new end time
                new_end_time = prompt_time("Enter new end time(HH:MM): ")

                # create datetime object
                end_datetime = datetime.combine(current.day, new_end_time)

                # make sure start time before end time
                if end_datetime > item_to_modify.start_time:
                    item_to_modify.end_time = end_datetime  # modify end time
                else:
                    print("Error, end time cannot be before start time. Exiting modification...")
                    return
            elif mod_choice == 3: # modify quality
                new_quality = get_sleep_quality()
                item_to_modify.quality = new_quality
            elif mod_choice == 4: # modify notes
                new_notes = input("Enter new notes on the sleep: ")
                item_to_modify.notes = new_notes
            elif mod_choice == 5:
                # call update function on exit
                db.update_sleep_session(item_to_modify)
                print("Exiting Current Sleep Modification...")

            # print updated sleep session data
            print()
            print(f"# Current Sleep Session #")
            print(current_list[choice - 1])

def delete_entry(entity:str):
    print(f"## Delete {entity} ## ")
    current = search_to_modify_or_delete()

    # if date doesn't exist in collection, print message and exit to main menu
    if not current:
        print("No entry found for this date")
        return

    # set variable for list
    current_list = ""
    if entity == "Meal":
        current_list = current.meals
    elif entity == "Workout":
        current_list = current.workouts
    elif entity == "Sleep":
        current_list = current.sleep_sessions

    # print menu, get user choice
    choice = 0
    while choice != (len(current_list) + 1):
        # print entries
        print_list_entries(current_list, entity)
        # print exit option
        print(f"{len(current_list) + 1}. Exit to main menu")

        # get user choice
        choice = prompt_int_range(f"{entity} to delete (or {len(current_list) + 1} to exit): ",
                                  1, len(current_list) + 1)
        # exit if user chooses to exit meal modification
        if choice == len(current_list) + 1:
            print(f"Exiting Delete {entity}...")
            return

        # delete meal/workout/sleep from list and save object returned from pop()
        item_to_remove = current_list.pop(choice-1)

        # remove from database via id number
        if entity == "Meal":
            db.delete_meal(item_to_remove.id)
        elif entity == "Workout":
            db.delete_workout(item_to_remove.id)
        elif entity == "Sleep":
            db.delete_sleep_session(item_to_remove.id)


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
        # get year input
        year = prompt_int("Enter year to filter: ")
        #day_list = db.filter_by_year(year)

        # build start and end dates, send to function to return list of days
        start_date = str(year) + "-01-01"
        end_date = str(year+1) + "-01-01"
        day_list = db.get_day_range(start_date, end_date)

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

        # get month input
        month = prompt_int_range("Enter month to filter (1-12): ", 1, 12)
        #day_list = db.filter_by_month(month, year)

        # build start and end dates, send to function to return list of days
        start_date = f"{year}-{month:02}-01"
        if month == 12:
            month = 0
            year += 1
        end_date = f"{year}-{month + 1:02}-01"
        day_list = db.get_day_range(start_date, end_date)

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
        # get date range input
        start_date = prompt_date("Enter start date (MM/DD/YYYY): ")
        end_date = prompt_date("Enter end date (MM/DD/YYYY): ")

        # while end date is not later than start date, prompt for input
        while end_date < start_date:
            print("Error, end date must come after start date")
            start_date = prompt_date("Enter start date: ")
            end_date = prompt_date("Enter end date: ")
        #day_list = db.filter_by_date_range(start_date, end_date)

        # build start and end dates, send to function to return list of days
        end_date = end_date + timedelta(days=1)
        day_list = db.get_day_range(str(start_date), str(end_date))

        # print list of entries found
        print(f"\n* Entries in date range")
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

    EXIT = 13
    choice = 0
    while choice != EXIT:
        # print menu - We will be adding to these as we go throughout the course
        print("### Health and Wellness App ###")
        print("1. Add Meal")
        print("2. Add Workout")
        print("3. Add Sleep")
        print("4. Search Date")
        print("5. Modify Meal")
        print("6. Delete Meal")
        print("7. Modify Workout")
        print("8. Delete Workout")
        print("9. Modify Sleep")
        print("10. Delete Sleep")
        print("11. Filter by Date")
        print("12. Load in from XML")
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
            add_sleep()
        elif choice == 4:
            search_entry()
        elif choice == 5:
            modify_attribute("Meal") # modify meal
        elif choice == 6:
            delete_entry("Meal") # delete meal
        elif choice == 7:
            modify_attribute("Workout") # modify workout
        elif choice == 8:
            delete_entry("Workout") # delete workout
        elif choice == 9:
            modify_sleep_attribute() # modify sleep
        elif choice == 10:
            delete_entry("Sleep") # delete sleep
        elif choice == 11:
            filter_by_date()
        elif choice == 12:
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

def prompt_time(prompt):
    while True:
        time_str = input(prompt)
        t = get_time(time_str)
        if t:
            return t
        print("Error, enter a valid time.")

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

def get_sleep_quality():
    # print list of sleep quality options, get user input
    print("Select Sleep Quality: ")
    for index, sleep_quality in enumerate(SleepQuality, start=1): # print options
        print(f"{index}. {sleep_quality}")

    choice = prompt_int_range("Choice: ", 1, len(SleepQuality))
    return list(SleepQuality)[choice - 1] # return sleep quality rating chosen by user

if __name__ == "__main__":
    main()