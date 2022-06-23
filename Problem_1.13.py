def distance(b):
    """ 1 foot = 1/3 yard = 12 dyuym = 0,3048 miles"""
    return f"{b} f = {b * 12} Dyuym", f"{b} f = {b * (1/ 3)} yard", f"{b} f = {b * (0.0002)} miles"

d = float(input("distance is foot: "))
print(distance(d))
