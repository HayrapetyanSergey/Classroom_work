def days_of_month(year, month):
    if  month in [1, 3, 5, 7, 8, 10, 12]:
        return  "31 days of month"
    elif month in [4, 6, 9, 11]:
        return "30 days of month"
    elif month == 2 and (year % 4 ==0 or year % 100 == 0):
        return "29 days of month"
    elif month == 2:
        return "28 dyas of month"

print(days_of_month(1996,2))