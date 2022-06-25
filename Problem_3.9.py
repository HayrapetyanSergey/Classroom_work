import random
def random_passwd(n):
    passwrd = ''
    for i in range(n):
        num = random.randint(33, 126)
        passwrd += chr(num)
    return passwrd


print(random_passwd(3))