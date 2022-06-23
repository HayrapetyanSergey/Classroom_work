def middle(n):
    average = sum(n) / len(n)
    small = []
    high = []
    for i in n:
        if i < average:
            small.append(i)
    for i in n:
        if i > average:
            high.append(i)

    return average, small, high

num = (input("Your numbers are: ").split(' '))
num = list(int(j) for j in num)
print(middle(num))
