def triangle_area(base, height):
    return f"area of triangle is {(base * height) / 2} m^2"

b = float(input("Base of triangle is: "))
h = float(input("Height of triangle is: "))
print(triangle_area(b, h))