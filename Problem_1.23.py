def season(month:str, day:int):
    winter = ['January', 'February', 'December']
    summer = ['June', 'July', 'August']
    autumn = ['September', 'November', 'October']
    spring = ['May', 'April', 'Mart']

    if month in winter:
        return('Winter')
    elif month in summer:
        return('Summer')
    elif month in autumn:
        return('Autumn')
    elif month in spring:
        return('Spring')    
    return "There is no such month"


name = str(input("Name of Month: "))
day = int(input("Day of Month: "))
print(season(name, day))