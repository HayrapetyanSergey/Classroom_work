def MPG(num):
    """ 1 gallon = 3.7 litr, 1 miles = 1.6 km, MPG = miles * gallon , l/100km = (gallon * 3.7) * 100 / (1.6 * miles) """
    return f"{num} MPG = {num *  235.21} l/100km"

n = int(input("MPG is: "))
print(MPG(n))