
import math


import math
def operations(a, b):
    return (f"sum is {a + b}", f"dis is {a - b}", f"div is {a / b}" ,f"int div is {a // b}",f"res is {a % b}",f"log base 10 is {math.log10(a)}") 

n = int(input("1st number is: "))
m = int(input("2nd number is: "))
print (operations(n, m))