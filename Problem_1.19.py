def count(day, time, min, sec):
    return (((((day * 24) + time) * 60) + min) * 60) + sec

d = int(input("Count of Days: "))
t = int(input("Count of times: "))
m = int(input("Count of min: "))
s = int(input("Count of sec: "))
print(count(d, t, m, s))