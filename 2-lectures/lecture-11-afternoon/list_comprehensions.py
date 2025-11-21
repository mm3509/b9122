def is_leap_year(year):

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0


print([is_leap_year(year) for year in range(1900, 2026)])
