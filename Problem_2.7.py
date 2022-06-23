def is_sorted(result):
    if sorted(result) == result:
        return True
    elif sorted(result)==result[::-1]:
        return True
    else:
        return False

res = [int(i) for i in input("input nums: ").split()]
print(is_sorted(res)) 