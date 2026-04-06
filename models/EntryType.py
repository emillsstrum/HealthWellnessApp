from enum import Enum

class MealType(Enum): # enumerations for type of meal
    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    SNACK = "Snack"

    # __str__ method that returns each type not in all caps
    def __str__(self):
        return self.value

class WorkoutType(Enum): # enumerations for type of workout
    CARDIO = "Cardio"
    STRENGTH = "Strength"
    FLEXIBILITY = "Flexibility"
    HIGH_INTENSITY = "High Intensity"
    GROUP_FITNESS = "Group Fitness"
    OTHER = "Other"

    # __str__ method that returns each type not in all caps
    def __str__(self):
        return self.value

# test
def main():
    print(MealType.BREAKFAST)
    print(MealType.LUNCH)
    print(MealType.DINNER)
    print(MealType.SNACK)
    print(WorkoutType.CARDIO)
    print(WorkoutType.STRENGTH)
    print(WorkoutType.FLEXIBILITY)
    print(WorkoutType.HIGH_INTENSITY)
    print(WorkoutType.GROUP_FITNESS)
    print(WorkoutType.OTHER)

if __name__ == "__main__":
    main()