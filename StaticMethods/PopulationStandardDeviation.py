from StaticMethods.Exceptions import exception
from StaticMethods.CalulcateMean import calMean
from StaticMethods.addition import addition
from StaticMethods.division import division
from StaticMethods.roundOff import roundOff
from StaticMethods.square import square
from StaticMethods.squareroot import squareroot
from StaticMethods.subtraction import subtraction


def stddev(a):
    total = 0
    mean = calMean(a)

    for val in a:
        total = addition(square(subtraction(mean, val)), total)

    result = squareroot(division(len(a), total))
    return roundOff(result)

