def land_area(lenght, width):
    return f"The area of land is {(lenght * width) / 43560} akr "

l = float(input("The lenght is: "))
w = float(input("The width is: "))
print(land_area(l, w))
