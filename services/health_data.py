mealTracker = {} # each value is the calorie count for the meal
workoutTracker = {} # each entry is the calorie count burned from the workout

def add_meal(date, meal : dict):
    # if date is not already in mealTracker
    # add date and meal/calorie details to mealTracker
    if date in mealTracker:
        return False
    elif date not in mealTracker:
        mealTracker[date] = meal
        return True

def add_workout(date, workout : dict):
    # if date is not already in workoutTracker
    # add date and workout/calorie details to workoutTracker
    if date in workoutTracker:
        return False
    elif date not in workoutTracker:
        workoutTracker[date] = workout
        return True


