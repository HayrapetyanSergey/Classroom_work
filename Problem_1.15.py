import math
def cylinder_volume(h, r):
    return f"Volume of Cylinder is {math.pi * (r ** 2) * h:.2}"

h = float(input("Height is: "))
r = float(input("Radius is: "))
print(cylinder_volume(h, r))