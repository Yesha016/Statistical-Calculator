from StaticMethods.Exceptions import exception
from StaticMethods.division import division
from StaticMethods.roundOff import roundOff


def calMean(a):
    total = 0
    for val in a:
        exception(a)
        total += float(val)

    result = division(len(a), total)
    return roundOff(result)
