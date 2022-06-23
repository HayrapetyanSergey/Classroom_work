def restaurant(a):
    tip = (a * 18) / 100 
    duty = ((a + tip) * 20) / 100
    sum = a + duty + tip
    return f"tip is $ {tip}", f"Duty is $ {duty}", f"Sum is $ {sum}"

money = float(input("Your bill in restaurant is $  " ))
print(restaurant(money))