def game(n):
    if n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 3 != 0 and n % 5 == 0:
        return "Bizz"
    elif n % 3 == 0 and n % 5 == 0:
        return "Fizz-Bizz"
    else:
        return n + 1

num = int(input("Your number is: ")) 
print(game(num))