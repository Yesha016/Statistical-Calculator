from StaticMethods.Exceptions import exception
from StaticMethods.CalulcateMean import calMean

def stddev(a):
    total = 0
    mean = calMean(a)

    for val in a:
        total += (float(val) - mean) ** 2

    return round(float(total / len(a)) ** 0.5, 2)

