def Herons_formula(a, b, c):
    s = (a + b + c) / 2
    return f"Area of triangel is {(s * (s - a) * (s - b) * (s - c)) ** 0.5}"

a = float(input("1st side 0f triagle is: "))
b = float(input("2nd side 0f triagle is: "))
c = float(input("3th side 0f triagle is: "))
print(Herons_formula(a, b, c))