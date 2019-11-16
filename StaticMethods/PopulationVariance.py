from StaticMethods.PopulationStandardDeviation import stddev
from StaticMethods.roundOff import roundOff
from StaticMethods.square import square


def varpp(a):
    val = stddev(a)
    result = square(val)
    return roundOff(result)
