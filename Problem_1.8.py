def shop(h, m):
    return f"weight is {(h * 75) + (m * 112)}gr"

hush = int(input("count of hush:"))
manr = int(input("count of manr:"))

print(shop(hush,manr))