from collections import defaultdict
from StaticMethods.Exceptions import exception


def calMode(array):
    length = len(array)
    count = defaultdict(list)
    for i in range(length):
        count[array[i]].append(1)

    k = count[0]
    for i in count:
        if count[i] > k:
            k = count[i]
            mode = i

    return round(float(mode), 2)
