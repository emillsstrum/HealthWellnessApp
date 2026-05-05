import sqlite3
from datetime import date
from models.CalorieEntities import *
from models.DateEntity import Day

DATABASE_NAME = "health_data.db" # database filename

def get_connection() -> sqlite3.Connection:
    # get SQLite connection object
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    return conn

def add_meal_to_database(meal_date:date, meal:Meal) -> bool:
    # insert date and meal objects into meals table
    # get connection and cursor object
    conn = get_connection()
    cursor = conn.cursor()

    # try/except for SQL commands
    try:
        # insert into meals table
        cursor.execute("INSERT INTO meals (date, description, calories, meal_type) VALUES(?, ?, ?, ?)",
                       (meal_date, meal.description, meal.calories, str(meal.meal_type)))
        conn.commit()
        return True
    except Exception as e:
        # if exception, rollback
        print(e) #TODO comment out
        conn.rollback()
        return False
    finally:
        # close connection
        conn.close()

def add_workout_to_database(workout_date:date, workout:Workout) -> bool:
    # insert date and workout objects into workouts table
    # get connection and cursor object
    conn = get_connection()
    cursor = conn.cursor()

    # try/except for SQL commands
    try:
        # insert into workouts table
        cursor.execute("INSERT INTO workouts (date, description, calories, workout_type) VALUES(?, ?, ?, ?)",
                       (workout_date, workout.description, workout.calories, str(workout.workout_type)))
        conn.commit()
        return True
    except Exception as e:
        # if exception, rollback
        print(e) #TODO comment out
        conn.rollback()
        return False
    finally:
        # close connection
        conn.close()

def get_day(search_date:date) -> Day | None:
    # search for meals and workouts by date
    # get connection and cursor object
    conn = get_connection()
    cursor = conn.cursor()

    # get all columns from meals table with matching date
    cursor.execute("SELECT * FROM meals WHERE date = ?", (search_date,))
    meals_found = cursor.fetchall()

    # get all columns from workout table with matching date
    cursor.execute("SELECT * FROM workouts WHERE date = ?", (search_date,))
    workouts_found = cursor.fetchall()

    # if no meals or workouts found return None
    if meals_found is None and workouts_found is None:
        return None

    # create Day object
    day = Day(search_date)

    # add meals and workouts to lists
    meals = [Meal(meal[2], meal[3], MealType(meal[4]), meal[0]) for meal in meals_found]
    workouts = [Workout(workout[2], workout[3], WorkoutType(workout[4]), workout[0]) for workout in workouts_found]

    # assign lists to Day object
    day.meals = meals
    day.workouts = workouts

    # return Day object
    return day