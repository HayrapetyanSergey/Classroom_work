number = None
count = 0
res = 0
while number != 0:
    number = int(input('Enter numbers: '))
    count += 1
    res += number

print(res / (count-1))