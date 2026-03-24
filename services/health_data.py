mealTracker = {} # each value is the calorie count for the meal
workoutTracker = {} # each entry is the calorie count burned from the workout

def add_meal(date, meal : dict):
    # if date is not already in mealTracker
    # add date and meal/calorie details to mealTracker
    if date not in mealTracker:
        mealTracker[date] = meal
        return True
    return False

def add_workout(date, workout : dict):
    # if date is not already in workoutTracker
    # add date and workout/calorie details to workoutTracker
    if date not in workoutTracker:
        workoutTracker[date] = workout
        return True
    return False

def get_meal(date):
    # if date exists in mealTracker return meal data
    if date in mealTracker:
        return mealTracker.get(date)
    return None

def get_workout(date):
    # if date exists in workoutTracker return workout data
    if date in workoutTracker:
        return workoutTracker.get(date)
    return None

def main():
    date = input("enter date: ")
    workout_details = input("enter workout details: ")
    calories_burned = input("enter calories burned: ")
    workout = {"workout_details":workout_details, "calorie_count":calories_burned}
    add_workout(date, workout)
    print(workoutTracker)

if __name__ == "__main__":
    main()
