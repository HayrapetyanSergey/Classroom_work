def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def first_prime(num):
    while not is_prime(num):
        num += 1
    return num 

print(first_prime(7))