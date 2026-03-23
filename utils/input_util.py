from datetime import date

def get_int(num) -> int | None:
    # convert string value to int
    try:
        return int(num)
    except ValueError: # if exception thrown return None
        return None

def get_int_range(num, low, high) -> int | None:
    # convert string value to int
    value = get_int(num)
    # return value if not None and in range
    if value is None:
        return None
    if value < low or value > high:
        return None
    return value

def get_float(num) -> float | None:
    # convert string value to float
    try:
        return float(num)
    except ValueError: # if exception thrown return None
        return None

def get_date(str_date : str) -> date | None:
    # convert string to date if string in MM/DD/YYYY format
    if len(str_date) == 10 and str_date[2] == '/' and str_date[5] == '/':
        split_date = str_date.split("/")
        month = get_int(split_date[0])
        day = get_int(split_date[1])
        year = get_int(split_date[2])
        if month and day and year:
            try:
                return date(year, month, day)
            except ValueError:
                return None
    else:
        return None

def main():
    # test get_int()
    print("* test get_int")
    print(get_int("6"))
    print(get_int("six"))
    # test get_int_range()
    print()
    print("* test get_int_range")
    print(get_int_range("6", 0, 10))
    print(get_int_range("11", 0, 10))
    print(get_int_range("-1", 0, 10))
    # test get_date()
    print()
    print("* test get_date")
    print(get_date("03/16/1995"))
    print(get_date("16/03/1995"))
    print(get_date("March 16, 1995"))

if __name__ == "__main__":
    main()