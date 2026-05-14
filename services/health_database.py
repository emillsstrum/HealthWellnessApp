import sqlite3
from datetime import date, datetime
from models.CalorieEntities import *
from models.DateEntity import Day
from models.SleepEntity import SleepQuality, SleepSession

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
        print(e)
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
        print(e)
        conn.rollback()
        return False
    finally:
        # close connection
        conn.close()

def add_sleep_session_to_database(sleep_date:date, sleep:SleepSession) -> bool:
    # insert date and sleep_session objects into sleep_sessions table
    # get connection and cursor object
    conn = get_connection()
    cursor = conn.cursor()

    # try/except for SQL commands
    try:
        # insert into sleep_sessions table
        cursor.execute("""INSERT INTO sleep_sessions (date, start_time, end_time, sleep_quality, notes) 
                          VALUES(?, ?, ?, ?, ?)""",
                       (sleep_date, sleep.start_time, sleep.end_time, str(sleep.quality), sleep.notes))
        conn.commit()
        return True
    except Exception as e:
        # if exception, rollback
        print(e)
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

    # get all columns from sleep_sessions table with matching date
    cursor.execute("SELECT * FROM sleep_sessions WHERE date = ?", (search_date,))
    sleeps_found = cursor.fetchall()

    # if no meals, workouts, or sleeps found return None
    if meals_found is None and workouts_found is None and sleeps_found is None:
        return None

    # create Day object
    day = Day(search_date)

    # add meals and workouts to lists
    meals = [Meal(meal[2], meal[3], MealType(meal[4]), meal[0]) for meal in meals_found]
    workouts = [Workout(workout[2], workout[3], WorkoutType(workout[4]), workout[0]) for workout in workouts_found]
    sleeps = [SleepSession(parse_datetime(sleep[2]), parse_datetime(sleep[3]),SleepQuality([4]), sleep[5], sleep[0])
              for sleep in sleeps_found]

    # assign lists to Day object
    day.meals = meals
    day.workouts = workouts
    day.sleep_sessions = sleeps

    # return Day object
    return day

def get_day_range(start_date:str, end_date:str) -> list:
    # queries tables for meals and workouts in date range, returns list of day objects
    # get connection and cursor object
    conn = get_connection()
    cursor = conn.cursor()

    # get meals in date range
    cursor.execute("SELECT * FROM meals WHERE date >= ? AND date < ? ORDER BY date",
                   (start_date, end_date))

    meals = cursor.fetchall()

    # get workouts in date range
    cursor.execute("SELECT * FROM workouts WHERE date >= ? AND date < ? ORDER BY date",
                   (start_date, end_date))

    workouts = cursor.fetchall()

    # get sleep sessions in date range
    cursor.execute("SELECT * FROM sleep_sessions WHERE date >= ? AND date < ? ORDER BY date",
                   (start_date, end_date))

    sleeps = cursor.fetchall()

    # if meals and workouts tuples empty, return empty list
    if len(meals) == 0 and len(workouts) == 0 and len(sleeps) == 0:
        return []

    # dictionary to hold items in range
    dict_of_days = {}

    # loop through meals, adding date as key and day object as value to dict
    for meal in meals:
        meal_date = parse_date(meal[1])
        # if not in dictionary, add date as key & new Day object as value
        if meal_date not in dict_of_days:
            dict_of_days[meal_date] = Day(meal_date)
        # add meal to day object
        dict_of_days[meal_date].add_meal(Meal(meal[2], meal[3], MealType(meal[4]), meal[0]))

    # loop through workouts, adding date as key and day object as value to dict
    for workout in workouts:
        workout_date = parse_date(workout[1])
        # if not in dictionary, add date as key & new Day object as value
        if workout_date not in dict_of_days:
            dict_of_days[workout_date] = Day(workout_date)
        # add workout to day object
        dict_of_days[workout_date].add_workout(Workout(workout[2], workout[3], WorkoutType(workout[4]), workout[0]))

    # loop through sleeps, adding date as key and day object as value to dict
    for sleep in sleeps:
        sleep_date = parse_date(sleep[1])
        # if not in dictionary, add date as key & new Day object as value
        if sleep_date not in dict_of_days:
            dict_of_days[sleep_date] = Day(sleep_date)
        # add sleep to day object
        dict_of_days[sleep_date].add_sleep_session(SleepSession(
            parse_datetime(sleep[2]), parse_datetime(sleep[3]),SleepQuality([4]), sleep[5], sleep[0]))

    # return list of dictionary values
    return list(dict_of_days.values())

def parse_date(date_str:str) -> date:
    # parses date string to date object
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def parse_datetime(datetime_text:str) -> datetime:
    # parses string into datetime object
    return datetime.strptime(datetime_text, "%Y-%m-%d %H:%M:%S.%f")

def update_meal(meal:Meal) -> bool:
    # update meals table with modified attributes, returns true if successful
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # update table
        cursor.execute("UPDATE meals SET description = ?, calories = ?, meal_type = ? WHERE id = ?",
                       (meal.description, meal.calories, str(meal.meal_type), meal.id))

        conn.commit()
        return cursor.rowcount == 1 # returns true if 1 row updated
    except Exception:
        conn.rollback()
        return False
    finally:
        conn.close()

def update_workout(workout:Workout) -> bool:
    # update workouts table with modified attributes
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # update table
        cursor.execute("UPDATE workouts SET description = ?, calories = ?, workout_type = ? WHERE id = ?",
                       (workout.description, workout.calories, str(workout.workout_type), workout.id))

        conn.commit()
        return cursor.rowcount == 1  # returns true if 1 row updated
    except Exception:
        conn.rollback()
        return False
    finally:
        conn.close()

def update_sleep_session(sleep:SleepSession) -> bool:
    # update sleep_sessions table with modified attributes
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # update table
        cursor.execute("""UPDATE sleep_sessions SET start_time = ?, end_time = ?, sleep_quality = ?, notes = ?, 
                        WHERE id = ?""",
                       (sleep.start_time, sleep.end_time, str(sleep.quality), sleep.notes, sleep.id))

        conn.commit()
        return cursor.rowcount == 1  # returns true if 1 row updated
    except Exception:
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_meal(meal_id:int):
    # delete meal from table, return true if successful
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # delete meal from table
        cursor.execute("DELETE FROM meals WHERE id = ?", (meal_id,))
        conn.commit()
        return cursor.rowcount == 1
    except Exception:
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_workout(workout_id:int):
    # delete workout from table, return true if successful
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # delete workout from table
        cursor.execute("DELETE FROM workouts WHERE id = ?", (workout_id,))
        conn.commit()
        return cursor.rowcount == 1
    except Exception:
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_sleep_session(ss_id:int):
    # delete sleep session from table, return true if successful
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # delete sleep session from table
        cursor.execute("DELETE FROM sleep_sessions WHERE id = ?", (ss_id,))
        conn.commit()
        return cursor.rowcount == 1
    except Exception:
        conn.rollback()
        return False
    finally:
        conn.close()













