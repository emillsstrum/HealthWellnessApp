import sqlite3
from datetime import date
from models.CalorieEntities import *

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