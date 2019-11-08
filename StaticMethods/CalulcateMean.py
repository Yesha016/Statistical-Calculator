from StaticMethods.Exceptions import exception
from StaticMethods.roundOff import roundOff


def calMean(a):
    total = 0
    for val in a:
        exception(a)
        total += float(val)

    return roundOff(total / len(a))
