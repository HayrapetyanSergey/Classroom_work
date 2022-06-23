def month(name:str):
    day_31 = ['January', 'December', 'July', 'August', 'October', 'May', 'Mart']
    day_30 = ['April','June','September','November']
    if name in day_31:
        return "days of month are 31"
    elif name in day_30:
        return "days of month are 30"
    elif name == "February":
        return "days of month are 28 or 29"
    return "There is no such month"

word = str(input("Name of month is: "))
print(month(word))