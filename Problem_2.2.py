def divisor(n):
    return [i for i in range(1, n) if n % i == 0]

print(divisor(24))