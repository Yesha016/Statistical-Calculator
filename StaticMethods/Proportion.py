from StaticMethods.division import division
from StaticMethods.roundOff import roundOff


def proportion(size, corr):
    if corr is None:
        corr = 10

    result = division(corr, size)

    return roundOff(result)
