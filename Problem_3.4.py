def is_even_index(data):
    lst = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            lst.append(i)
    return f"index is: {lst}"

lst = [1, 2, 3, 5, 6, 7, 10]
print(is_even_index(lst))