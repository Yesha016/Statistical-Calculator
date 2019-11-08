# from statistics import mean
from StaticMethods.CalulcateMean import calMean


class StatisticCal:
    result = 0

    def __init__(self):
        pass

    def mean(self, a):
        self.result = calMean(a)
        return self.result
