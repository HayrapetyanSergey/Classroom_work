def is_palindrom(str):
    signs = '`,.;:'
    clean_str = ""
    for i in str:
        if not i in signs:
            clean_str += i
    
    data = clean_str.split(" ")

    for j in range((len(data) // 2) + 1):
        data[j] = data[j].lower()
        if not data[j] == data[len(data) - j - 1]:
            return False
    return True

string = str(input("Your string: "))
print(is_palindrom(string))