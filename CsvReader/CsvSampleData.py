def randomData(val):
    data = []
    random = [1, 4, 6, 10, 13]
    for i in range(len(val)):
        if i in random:
            data.append(val[i])
    return data
