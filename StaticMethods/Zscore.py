from StaticMethods.Exceptions import exception
from StaticMethods.CalulcateMean import calMean
from StaticMethods.PopulationStandardDeviation import stddev

def zscore(a, mean, sd):

    result = round((float(a) - float(mean)) / float(sd), 2)
    return result
