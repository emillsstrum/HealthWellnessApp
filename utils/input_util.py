from datetime import date, datetime

list_of_months = ["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"]

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

def get_datetime(str_date : str) -> datetime:
    # convert string to datetime object
    return datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S.%f")