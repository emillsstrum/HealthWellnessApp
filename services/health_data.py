from models.DateEntity import Day
from models.CalorieEntities import Meal, Workout
from models.EntryType import MealType, WorkoutType
from datetime import date

health_data = {} # dictionary to hold date/meal/workout data

def add_meal(date_input : date, meal : Meal):
    # if date (key) is in health_data, use to get Day object (value) in health_data
    # call add_meal() method of Day object (appends Meal object to meals list)
    if date_input in health_data:
        health_data[date_input].add_meal(meal)
        return True
    return False

def add_workout(date_input : date, workout : Workout):
    # if date (key) is in health_data, use to get Day object (value) in health_data
    # call add_workout() method of Day object (appends Workout object to workouts list)
    if date_input in health_data:
        health_data[date_input].add_workout(workout)
        return True
    return False

#def get_meal(date):
    # if date exists in mealTracker return meal data
    #if date in mealTracker:
    #    return mealTracker.get(date)
    #return None

#def get_workout(date):
    # if date exists in workoutTracker return workout data
    #if date in workoutTracker:
    #    return workoutTracker.get(date)
    #return None

def get_entry(date_input : date):
    # if date exists in health_data, return Day object
    if date_input in health_data:
        return health_data[date_input]
    return None

def add_day(date_input : date):
    # if date/day don't already exist in health_data, create Day object and add it to health_data
    if date_input not in health_data:
        health_data[date_input] = Day(date_input)
        return True
    return False

def filter_by_year(year:int) -> list[Day] :
    days = [value for value in health_data.values()]
    return [d for d in days if d.day.year == year]

def filter_by_month(month:int) -> list[Day] :
    days = [value for value in health_data.values()]
    return [d for d in days if d.day.month == month and d.day.year == date.today().year]

def filter_by_date_range(start:date, end:date) -> list[Day] :
    days = [value for value in health_data.values()]
    return [d for d in days if start <= d.day <= end]

def load_test_data():
    """Load 30 days of test data into health_data (selected dates in 2026)"""

    # Define sample meals with calorie values
    meals_data = [
        # Breakfast options
        ("Scrambled eggs with toast", 450, MealType.BREAKFAST),
        ("Oatmeal with berries", 350, MealType.BREAKFAST),
        ("Pancakes with syrup", 550, MealType.BREAKFAST),
        ("Yogurt and granola", 300, MealType.BREAKFAST),

        # Lunch options
        ("Chicken sandwich", 650, MealType.LUNCH),
        ("Caesar salad with grilled chicken", 550, MealType.LUNCH),
        ("Turkey and cheese wrap", 600, MealType.LUNCH),
        ("Pasta primavera", 700, MealType.LUNCH),
        ("Sushi rolls", 500, MealType.LUNCH),

        # Dinner options
        ("Grilled salmon with vegetables", 750, MealType.DINNER),
        ("Beef steak with mashed potatoes", 850, MealType.DINNER),
        ("Chicken stir fry with brown rice", 700, MealType.DINNER),
        ("Spaghetti with marinara sauce", 800, MealType.DINNER),
        ("Fish tacos", 650, MealType.DINNER),

        # Snack options
        ("Apple with almond butter", 250, MealType.SNACK),
        ("Protein bar", 200, MealType.SNACK),
        ("Mixed nuts", 280, MealType.SNACK),
    ]

    # Define sample workouts with calorie values
    workouts_data = [
        ("Morning walk", 250, WorkoutType.CARDIO),
        ("Evening walk", 200, WorkoutType.CARDIO),
        ("Running 3 miles", 400, WorkoutType.CARDIO),
        ("Cycling 30 minutes", 350, WorkoutType.CARDIO),
        ("Weight lifting - Upper body", 300, WorkoutType.STRENGTH),
        ("Weight lifting - Lower body", 320, WorkoutType.STRENGTH),
        ("Yoga session", 200, WorkoutType.FLEXIBILITY),
        ("HIIT workout", 500, WorkoutType.HIGH_INTENSITY),
        ("Spin class", 450, WorkoutType.GROUP_FITNESS),
        ("Zumba class", 400, WorkoutType.GROUP_FITNESS),
        ("Swimming", 380, WorkoutType.CARDIO),
        ("Hiking", 420, WorkoutType.CARDIO),
    ]

    # Set list of 30 specific dates in 2026
    test_dates = [
        date(2026, 1, 5), date(2026, 1, 12), date(2026, 1, 19), date(2026, 1, 26),
        date(2026, 2, 3), date(2026, 2, 10), date(2026, 2, 17), date(2026, 2, 24),
        date(2026, 3, 5), date(2026, 3, 12), date(2026, 3, 19), date(2026, 3, 26),
        date(2026, 4, 2), date(2026, 4, 9), date(2026, 4, 16), date(2026, 4, 23),
        date(2026, 5, 7), date(2026, 5, 14), date(2026, 5, 21), date(2026, 5, 28),
        date(2026, 6, 4), date(2026, 6, 11), date(2026, 6, 18), date(2026, 6, 25),
        date(2026, 7, 9), date(2026, 7, 16), date(2026, 7, 23), date(2026, 7, 30),
        date(2026, 8, 6), date(2026, 8, 13),
    ]

    # Meal pattern options
    meal_patterns = [
        [(MealType.BREAKFAST, 0), (MealType.LUNCH, 4), (MealType.DINNER, 10)],  # Breakfast, Lunch, Dinner
        [(MealType.LUNCH, 5), (MealType.DINNER, 11)],  # Lunch, Dinner
        [(MealType.LUNCH, 6), (MealType.SNACK, 15), (MealType.DINNER, 12)],  # Lunch, Snack, Dinner
    ]

    for day_index, current_date in enumerate(test_dates):
        # Add the day to health_data
        add_day(current_date)

        # Select meal pattern for the day
        meal_pattern_index = day_index % len(meal_patterns)
        meal_pattern = meal_patterns[meal_pattern_index]

        # Add meals based on pattern
        for meal_type, meal_idx in meal_pattern:
            meal = Meal(meals_data[meal_idx][0], meals_data[meal_idx][1], meal_type)
            add_meal(current_date, meal)

        # Add workouts - always include walking, occasionally add another workout
        # Always add a walk
        walk_workout = Workout("Morning walk", 250 if day_index % 2 == 0 else 200, WorkoutType.CARDIO)
        add_workout(current_date, walk_workout)

        # Add a second workout on most days
        if day_index % 2 == 0:  # Every other day
            second_workout_idx = (day_index + 1) % len(workouts_data)
            workout_data = workouts_data[second_workout_idx]
            workout = Workout(workout_data[0], workout_data[1], workout_data[2])
            add_workout(current_date, workout)

        # Occasionally add a third workout
        if day_index % 5 == 0:  # Every 5 days
            third_workout_idx = (day_index + 2) % len(workouts_data)
            workout_data = workouts_data[third_workout_idx]
            workout = Workout(workout_data[0], workout_data[1], workout_data[2])
            add_workout(current_date, workout)