from collections import defaultdict
from StaticMethods.roundOff import roundOff


def calMode(array):
    length = len(array)
    count = defaultdict(list)
    mode = 0
    for i in range(length):
        count[array[i]].append(1)

    k = count[0]
    for i in count:
        print("i: ", i)
        print("k: ", k)
        print("count: ",count[i])
        if count[i] > k:
            k = count[i]
            mode = i
    # TODO: Add condition to check if multiple value has highest numbers
    return roundOff(mode)
