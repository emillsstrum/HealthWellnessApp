from datetime import date

from models import SleepEntity
from models.CalorieEntities import Meal
from models.CalorieEntities import Workout
from models.SleepEntity import SleepSession, SleepQuality


class Day:
    def __init__(self, day : date): # create day object
        self.__day = day
        self.__meals = [] # create empty list for meals
        self.__workouts = [] # create empty list for workouts
        self.__sleep_sessions = [] # empty list for sleep sessions

    @property
    def day(self): # get the day/date property
        return self.__day
    @day.setter
    def day(self, value : date): # set the day/date property
        self.__day = value

    @property
    def meals(self) -> list: # get meals property
        return self.__meals
    @meals.setter
    def meals(self, value : list): # set meals property
        self.__meals = value

    @property
    def workouts(self) -> list:  # get workouts property
        return self.__workouts
    @workouts.setter
    def workouts(self, value: list): # set workouts property
        self.__workouts = value

    @property
    def sleep_sessions(self) -> list:  # get sleep sessions property
        return self.__sleep_sessions
    @sleep_sessions.setter
    def sleep_sessions(self, value: list):  # set sleep sessions property
        self.__sleep_sessions = value

    def add_meal(self, meal : Meal):
        # add Meal object to meals list
        self.__meals.append(meal)

    def add_workout(self, workout : Workout):
        # add Workout object to workouts list
        self.__workouts.append(workout)

    def add_sleep_session(self, sleep_session : SleepSession):
        # add sleep session to list
        self.__sleep_sessions.append(sleep_session)

    def remove_sleep_session(self, index : int):
        # remove sleep session from list
        if 0 <= index < len(self.__sleep_sessions):
            return self.__sleep_sessions.pop(index)
        return None

    def meal_calories(self):
        # use list comprehension to add up total calories consumed for the day
        return sum([meal.calories for meal in self.meals])
        #total_calories = 0
        #for meal in self.meals:
        #    total_calories += meal.calories
        #return total_calories

    def workout_calories(self):
        # add up total calories burned for the day
        return sum([workout.calories for workout in self.workouts])
        #total_calories = 0
        #for workout in self.workouts:
        #    total_calories += workout.calories
        #return total_calories

    def net_calories(self) -> int :
        # subtract workout calories from meal calories, return net calories
        net_calories = self.meal_calories() - self.workout_calories()
        return net_calories

    def sleep_duration_seconds(self):
        # total up sleep durations in seconds
        return sum([sleep_session.duration().seconds for sleep_session in self.sleep_sessions])

    def sleep_duration_hours_minutes(self) -> str:
        # convert total sleep seconds to hours and minutes
        duration_seconds = self.sleep_duration_seconds()
        duration_hours = duration_seconds // 3600  # get hours
        duration_minutes = duration_seconds % 3600 // 60  # get minutes

        return f"{duration_hours:.0f} Hours {duration_minutes:.0f} Minutes"

    def average_sleep_quality(self):
        # return average sleep quality rating
        total = 0

        # avoid dividing by zero error
        if len(self.sleep_sessions) == 0:
            return None

        # find sum and average
        for sleep_session in self.sleep_sessions:
            total += sleep_session.quality.value
        average_value = round(total / len(self.sleep_sessions))

        # return sleep quality enum
        if average_value == 1:
            return SleepQuality.VERY_POOR
        elif average_value == 2:
            return SleepQuality.POOR
        elif average_value == 3:
            return SleepQuality.FAIR
        elif average_value == 4:
            return SleepQuality.GOOD
        elif average_value == 5:
            return SleepQuality.EXCELLENT


    def __eq__(self, other):
        return self.__day == other.day

    def __str__(self):
        # print out date, meals, workouts, sleep sessions
        return f"Date: {self.day}\nMeals: {self.meals_to_string()}\nWorkouts: {self.workouts_to_string()}"\
                f"\nNet Calories: {self.net_calories()}\nSleeps: {self.sleep_sessions_to_string()}"\
                f"\nTotal Sleep: {self.sleep_duration_hours_minutes()}\nAverage Sleep Quality: "\
                f"{self.average_sleep_quality()}"

    def meals_to_string(self):
        # create string of meals
        string = ""
        for meal in self.meals:
            string += "\n\t" + str(meal)
        return string

    def workouts_to_string(self):
        # create string of workouts
        string = ""
        for workout in self.workouts:
            string += "\n\t" + str(workout)
        return string

    def sleep_sessions_to_string(self):
        # create string of sleep sessions
        string = ""
        for sleep_session in self.sleep_sessions:
            string += "\n\t" + str(sleep_session)
        return string

    def to_dict(self) -> dict: # create dictionary for object
        # create lists of meal and workout dictionaries
        meals_dictionary = [meal.to_dict() for meal in self.meals]
        workouts_dictionary = [workout.to_dict() for workout in self.workouts]
        # create dictionary for Day object
        return {"date": self.day.strftime("%m/%d/%Y"), "meals": meals_dictionary, "workouts": workouts_dictionary}

    def to_report(self): # for CSV report
        # return dictionary of date, total meal/workout calories for day, net calories, total sleep, & average quality
        return {"Date": self.day.strftime("%m/%d/%Y"), "Meal Calories": self.meal_calories(),
                "Workout Calories": self.workout_calories(), "Net Calories": self.net_calories(),
                "Total Sleep": self.sleep_duration_hours_minutes(), "Average Sleep Quality": self.average_sleep_quality()}