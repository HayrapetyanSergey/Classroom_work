def median(data):
    if len(data) % 2 != 0:
        return data[int(len(data) / 2)]
    else:
        return (data[int(len(data) / 2) - 1] + data[int(len(data) / 2)]) / 2


print(median([10, 20, 15, 24, 38, 36]))