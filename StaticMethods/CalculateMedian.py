from StaticMethods.Exceptions import exception
from StaticMethods.addition import addition
from StaticMethods.division import division
from StaticMethods.roundOff import roundOff


def calMedian(a):
    length = len(a)
    half = int(division(2, length))

    for val in a:
        exception(val)

    if length % 2 == 0:
        median = division(2, addition(a[half - 1], a[half]))
    else:
        median = a[half]

    return roundOff(median)
