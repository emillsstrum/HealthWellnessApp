from datetime import datetime
from enum import IntEnum


class SleepSession: # object to help track sleep
    def __init__(self, start_time:datetime, end_time:datetime, quality:SleepQuality, notes:str, entry_id=0):
        self.start_time = start_time
        self.end_time = end_time
        self.quality = quality
        self.__notes = notes
        self.__id = entry_id

    # getter and setter for start_time
    @property
    def start_time(self):
        return self.__start_time
    @start_time.setter
    def start_time(self, value):
        # validation - check if value is datetime object and before end time
        if isinstance(value, datetime) and value < self.__end_time:
            self.__start_time = value
        else: # if value not datetime set as default
            self.__start_time = datetime.now() # TODO is this right?

    # getter and setter for end_time
    @property
    def end_time(self):
        return self.__end_time
    @end_time.setter
    def end_time(self, value):
        # validation - check if value is datetime object and after start time
        if isinstance(value, datetime) and value > self.__start_time:
            self.__end_time = value
        else: # if value not datetime set as default
            self.__end_time = datetime.now() # TODO is this right?

    # getter and setter for sleep quality
    @property
    def quality(self):
        return self.__quality
    @quality.setter
    def quality(self, value):
        if isinstance(value, SleepQuality): # check if value is sleep quality enum
            self.__quality = value
        else: # if value not enum type set as default
            self.__quality = SleepQuality.FAIR

    # getter and setter for notes
    @property
    def notes(self):
        return self.__notes
    @notes.setter
    def notes(self, value):
        self.__notes = value

    # getter for id
    @property
    def id(self):
        return self.__id

class SleepQuality(IntEnum): # enumerations for sleep quality rating
    VERY_POOR = 1
    POOR = 2
    FAIR = 3
    GOOD = 4
    EXCELLENT = 5

    # __str__ method to return text values
    def __str__(self):
        if self.value == 1:
            return "Very Poor"
        elif self.value == 2:
            return "Poor"
        elif self.value == 3:
            return "Fair"
        elif self.value == 4:
            return "Good"
        elif self.value == 5:
            return "Excellent"

# test
def main():
    print(SleepQuality.VERY_POOR)
    print(SleepQuality.VERY_POOR.name)
    print(SleepQuality.VERY_POOR.value)


if __name__ == '__main__':
    main()