# from statistics import mean
from StaticMethods.CaclulateMode import calMode
from StaticMethods.CalculateMedian import calMedian
from StaticMethods.CalulcateMean import calMean


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
