class HealthEntry: # base class for Meal / Workout classes
    def __init__(self, description:str, calories:int):
        self._description = description
        self.calories = calories

    # getter and setter for description
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value

    # getter and setter for calories
    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, value):
        if value > 0:
            self._calories = value

    # set up string method
    def __str__(self):
        return f"Entry: {self._description}, Calories: {self._calories}"

# test
def main():
    description = input("Enter a description: ")
    calories = int(input("Enter calories: "))
    entry = HealthEntry(description, calories)
    print(entry)

if __name__ == "__main__":
    main()