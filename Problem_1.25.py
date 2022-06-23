def temp(celsius):
    return f"Fahrenheit list {[(celsius[i] * 9 / 5) + 32 for i in range(len(celsius))]}" 

num = [None] * 10
for i in range(len(num)):
    num[i] = int(input("Enter temp: "))

print(temp(num))