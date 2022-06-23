def speed(d):
    return f"Speed of last moment is {(2 * (9.8 ** 2) * d) ** 0.5} m/v"

d = float(input("Distance is: "))
print(speed(d))