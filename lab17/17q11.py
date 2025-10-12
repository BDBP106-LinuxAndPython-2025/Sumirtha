def is_magic_date(month, day, year):
    year_last_two = year % 100
    return month * day == year_last_two
def days_in_month(month, year):
     if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return 30
