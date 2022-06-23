def bottle(small, big):
    return f" $ {(small * 0.10) + (big * 0.25):.2}"

s = int(input("smaller bottles are: "))
b = int(input("big bottles are: "))
print(bottle(s, b))