def zip(data1, data2):
    new_list = [None] * len(data1) 
    for i in range(len(data1)):
        new_list[i] = [data1[i], data2[i]]
    return new_list

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
print(zip(a, b))