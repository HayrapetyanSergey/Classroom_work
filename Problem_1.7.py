def sum(n):
    i = 0
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum
    
m = int(input())
print(sum(m))
