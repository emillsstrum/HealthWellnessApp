from unittest import TestCase
from models.HealthEntry import HealthEntry
from models.CalorieEntities import Meal, Workout
from models.EntryType import MealType, WorkoutType

class TestCalorieEntities(TestCase):
    # set up Meal and Workout test objects
    @classmethod
    def setUpClass(cls):
        cls.meal = Meal("Eggs and Bacon", 200, MealType.BREAKFAST)
        cls.workout = Workout("Lifted weights", 100, WorkoutType.STRENGTH)

    # test Meal calories setter
    def test_meal_calories_setter_positive(self):
        self.meal.calories = 50
        self.assertEqual(self.meal.calories, 50)

    def test_meal_calories_setter_negative(self):
        self.meal.calories = -50
        self.assertEqual(self.meal.calories, 0)

    # test Workout calories setter
    def test_workout_calories_setter_positive(self):
        self.workout.calories = 50
        self.assertEqual(self.workout.calories, 50)

    def test_workout_calories_setter_negative(self):
        self.workout.calories = -50
        self.assertEqual(self.workout.calories, 0)

    # test negative values in Meal constructor
    def test_meal_constructor_negative_calories(self):
        m2 = Meal("Bacon and Eggs", -50, MealType.BREAKFAST)
        self.assertEqual(m2.calories, 0)

    # test negative values in Workout constructor
    def test_workout_constructor_negative_calories(self):
        w2 = Workout("Lifted weights", -50, WorkoutType.STRENGTH)
        self.assertEqual(w2.calories, 0)

    # test meal type getter and setter
    def test_meal_type_getter(self):
        self.assertEqual(self.meal.meal_type, MealType.BREAKFAST)

    def test_meal_type_setter(self):
        self.meal.meal_type = MealType.LUNCH
        self.assertEqual(self.meal.meal_type, MealType.LUNCH)

    # test workout type getter and setter
    def test_workout_type_getter(self):
        self.assertEqual(self.workout.workout_type, WorkoutType.STRENGTH)

    def test_workout_type_setter(self):
        self.workout.workout_type = WorkoutType.CARDIO
        self.assertEqual(self.workout.workout_type, WorkoutType.CARDIO)

    # test invalid type for meal and workout type
    def test_meal_type_setter_invalid_type(self):
        self.meal.meal_type = "InvalidType"
        self.assertEqual(self.meal.meal_type, MealType.SNACK)

    def test_workout_type_invalid_type(self):
        self.workout.workout_type = "InvalidType"
        self.assertEqual(self.workout.workout_type, WorkoutType.OTHER)
