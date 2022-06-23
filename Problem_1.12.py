def height(d, f):
    return f"The height is {((d * 12) + f) * 2.54}sm"

d = float(input("Dyuym is: "))
f = float(input("Fut is: "))
print(height(d, f))