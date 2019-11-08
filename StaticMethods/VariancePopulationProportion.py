from StaticMethods.Exceptions import exception
from StaticMethods.PopulationStandardDeviation import stddev

def varpp(a):
    val = stddev(a)
    return round(float(val) ** 2, 2)