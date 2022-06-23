import math
def area_and_volume(r):
    return f"Circle area is {math.pi * (r ** 2)} and Cylinder volume is {(4 / 3) * (math.pi * (r ** 3))}"


r = float(input("Radius is: "))
print(area_and_volume(r))