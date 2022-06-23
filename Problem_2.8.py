from pickle import FALSE


def is_sublist(larger, smaller):
    if smaller == [] or smaller == larger:
        return True
    elif len(smaller) == 1:
        for i in range(len(larger)):
          if smaller == larger[i]:
                return True
        else:
            return False
    
    for i in range(len(smaller)):
        try:
            k = larger.index(smaller[i])
            if k + 1 != larger.index(smaller[i + 1]):
                return False
        except:
            pass
    return True

l = [1, 2, 3, 4, 5, 6]
s = [1, 2, 5, 3]

print(is_sublist(l, s))