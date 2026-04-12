from unittest import TestCase
from datetime import date
from models.DateEntity import Day
from models.EntryType import MealType, WorkoutType
from models.HealthEntry import HealthEntry
from models.CalorieEntities import Meal, Workout

class TestDayEntity(TestCase):
    @classmethod
    # set up test objects
    def setUpClass(cls):
        cls.day = Day(date(2026, 4, 12)) # create test Day object
        cls.meal = Meal("Bacon and Eggs", 200, MealType.BREAKFAST) # create test Meal object
        cls.workout = Workout("Lifted weights", 50, WorkoutType.STRENGTH) # create test Workout object
        # add Meal and Workout objects to Day object
        cls.day.meals = [cls.meal]
        cls.day.workouts = [cls.workout]

    # test net_calories method calculates correctly
    def test_net_calories_calculation(self):
        net_calories = self.day.net_calories()
        self.assertEqual(net_calories, "+150")

    # test __eq__ method
    def test_eq_method_equal(self):
        self.assertEqual(self.day, self.day)

    def test_eq_method_not_equal(self):
        day2 = Day(date(2026, 4, 13))
        self.assertNotEqual(self.day, day2)

    # test Day that has no meals/workouts
    def test_day_with_empty_calories(self):
        day2 = Day(date(2026, 4, 13))
        # check if calorie adding methods equal 0
        self.assertEqual(day2.meal_calories(), 0)
        self.assertEqual(day2.workout_calories(), 0)
        self.assertEqual(day2.net_calories(), "0")

    # test __str__ method
    def test_str_method_includes_labels(self):
        text = str(self.day)
        self.assertIn("Date:", text)
        self.assertIn("Meals:", text)
        self.assertIn("Workouts:", text)
        self.assertIn("Net Calories:", text)





