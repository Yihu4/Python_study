days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]


def how_many_days(month):
    return days_in_month[month - 1]


print(how_many_days(3))
print(how_many_days(8))
print(how_many_days(13))
