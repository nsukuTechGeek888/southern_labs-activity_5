#Author : Nsuku Bright Shikhibana

"""
This program contains functions that calculate the day of the week,
check for leap years, calculate year and month values, and process
the given date to return the correct day.
"""


def get_last_two_digits(year):
    """
    Gets the last two digits of the year.

    :param year: The year.
    :return: The last two digits of the year.
    """
    return year % 100


def get_number_of_twelves(last_two_digits):
    """
    Determines how many 12s fit into the last two digits.

    :param last_two_digits: The last two digits of the year.
    :return: The number of 12s that fit.
    """
    return last_two_digits // 12


def get_remainder(last_two_digits, number_of_twelves):
    """
    Calculates the remainder after dividing the last two digits by 12.

    :param last_two_digits: The last two digits of the year.
    :param number_of_twelves: The number of 12s that fit.
    :return: The remainder.
    """
    return last_two_digits - (number_of_twelves * 12)


def get_number_of_fours(remainder):
    """
    Determines how many 4s fit into the remainder.

    :param remainder: The remainder after dividing by 12.
    :return: The number of 4s that fit.
    """
    return remainder // 4


def get_month_code(month):
    """
    Gets the code for the given month.

    :param month: The month number.
    :return: The month code.
    """
    if month == 1:
        return 1
    elif month == 2:
        return 4
    elif month == 3:
        return 4
    elif month == 4:
        return 0
    elif month == 5:
        return 2
    elif month == 6:
        return 5
    elif month == 7:
        return 0
    elif month == 8:
        return 3
    elif month == 9:
        return 6
    elif month == 10:
        return 1
    elif month == 11:
        return 4
    else:
        return 6


def is_leap_year(year):
    """
    Determines whether a year is a leap year.

    :param year: The year.
    :return: True if the year is a leap year, otherwise False.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def get_year_offset(year):
    """
    Gets the special century offset for the year.

    :param year: The year.
    :return: The year offset.
    """
    if year >= 1600 and year < 1700:
        return 6
    elif year >= 1700 and year < 1800:
        return 4
    elif year >= 1800 and year < 1900:
        return 2
    elif year >= 2000 and year < 2100:
        return 6
    elif year >= 2100 and year < 2200:
        return 4
    else:
        return 0


def get_day_of_the_week(month, day, year):
    """
    Calculates the day of the week for a given date.

    :param month: The month number.
    :param day: The day of the month.
    :param year: The year.
    :return: The name of the day of the week.
    """
    last_two_digits = get_last_two_digits(year)

    number_of_twelves = get_number_of_twelves(last_two_digits)

    remainder = get_remainder(
        last_two_digits,
        number_of_twelves
    )

    number_of_fours = get_number_of_fours(remainder)

    month_code = get_month_code(month)

    year_offset = get_year_offset(year)

    if is_leap_year(year) and (month == 1 or month == 2):
        month_code = month_code + 6

    total = (
        number_of_twelves
        + remainder
        + number_of_fours
        + day
        + month_code
        + year_offset
    )

    day_number = total % 7

    if day_number == 0:
        return "Saturday"
    elif day_number == 1:
        return "Sunday"
    elif day_number == 2:
        return "Monday"
    elif day_number == 3:
        return "Tuesday"
    elif day_number == 4:
        return "Wednesday"
    elif day_number == 5:
        return "Thursday"
    else:
        return "Friday"


def main():
    """
    Tests the date calculation and gets a date from the user.
    """

    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))

    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the year: "))

    result = get_day_of_the_week(month, day, year)

    print(result)


if __name__ == "__main__":
    main()
