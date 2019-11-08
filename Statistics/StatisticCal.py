# from statistics import mean
from StaticMethods.CaclulateMode import calMode
from StaticMethods.CalculateMedian import calMedian
from StaticMethods.CalulcateMean import calMean
from StaticMethods.PopulationStandardDeviation import stddev
from StaticMethods.VariancePopulationProportion import varpp


class StatisticCal:
    result = 0

    def __init__(self):
        pass

    def mean(self, arr):
        self.result = calMean(arr)
        return self.result

    def median(self, arr):
        self.result = calMedian(arr)
        return self.result

    def mode(self, arr):
        self.result = calMode(arr)
        return self.result

    def sd(self, a):
        self.result = stddev(a)
        return self.result

    def vpp(self, a):
        self.result = varpp(a)
        return self.result