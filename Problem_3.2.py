def connect(num):
    res = ''
    for elem in num:
        res += elem
    return res

data = tuple(input("input numbers: ").split(' '))
print(connect(data))
