def same_parity(n, *args):
    res = []
    for i in args:
        if i % n == 0:
            res.append(i)
    return res

print(same_parity(2, 3, 4, 5, 6))