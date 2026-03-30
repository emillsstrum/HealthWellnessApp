class Meal:
    def __init__(self, items, calories): # create Meal object
        self.__items = items
        self.__calories = calories

    @property
    def items(self): # get the items property
        return self.__items
    @items.setter
    def items(self, value): # set the items property
        self.__items = value

    @property
    def calories(self): # get the calories property
        return self.__calories
    @calories.setter
    def calories(self, value): # set calories property if value > 0
        if value > 0:
            self.__calories = value

    def __str__(self):
        return f"Meal/Item: {self.items}, Calories: {self.calories}"

class Workout:
    def __init__(self, details, calories): # create Workout object
        self.__details = details
        self.__calories = calories

    @property
    def details(self): # get the details property
        return self.__details
    @details.setter
    def details(self, value): # set the details property
        self.__details = value

    @property
    def calories(self): # get the calories property
        return self.__calories
    @calories.setter
    def calories(self, value): # set calories property if value > 0
        if value > 0:
            self.__calories = value

    def __str__(self):
        return f"Workout: {self.details}, Calories Burned: {self.calories}"
