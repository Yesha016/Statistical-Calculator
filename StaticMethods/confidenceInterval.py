from StaticMethods.CalulcateMean import calMean
from StaticMethods.PopulationStandardDeviation import stddev
from StaticMethods.Zscore import zscore
from StaticMethods.division import division
from StaticMethods.multiplication import multiplication
from StaticMethods.roundOff import roundOff
from StaticMethods.squareroot import squareroot


def confidenceInterval(array):
    n = len(array)
    mean = calMean(array)
    sd = stddev(array)
    z = zscore(array[0], mean, sd)
    ci = mean + multiplication(division(squareroot(n), sd), z)

    return roundOff(ci)
