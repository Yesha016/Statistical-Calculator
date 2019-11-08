# from statistics import mean
from StaticMethods.CalculateMedian import calMedian
from StaticMethods.CalulcateMean import calMean
from StaticMethods.PopulationStandardDeviation import stddev
from StaticMethods.VariancePopulationProportion import varpp


class StatisticCal:
    result = 0

    def __init__(self):
        pass

    def mean(self, a):
        self.result = calMean(a)
        return self.result

    def median(self, a):
        self.result = calMedian(a)
        return self.result

    def sd(self, a):
        self.result = stddev(a)
        return self.result

    def vpp(self, a):
        self.result = varpp(a)
        return self.result