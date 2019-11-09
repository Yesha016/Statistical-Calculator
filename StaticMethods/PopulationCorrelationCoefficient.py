from StaticMethods.Exceptions import exception
from StaticMethods.CalulcateMean import calMean
from StaticMethods.PopulationStandardDeviation import stddev
from StaticMethods.addition import addition
from StaticMethods.division import division
from StaticMethods.multiplication import multiplication
from StaticMethods.roundOff import roundOff
from StaticMethods.subtraction import subtraction


def calcPCC(xArray, yArray):
    xMean = calMean(xArray)
    yMean = calMean(yArray)
    length = len(xArray)
    xSd = stddev(xArray)
    ySd = stddev(xArray)
    total = 0

    for i in range(0, length):
        total = addition(total, multiplication(division(xSd, subtraction(xMean, xArray[i])), division(ySd, subtraction(yMean, yArray[i]))))
        # total = subtraction(xMean, yArray[i])
    res = division(length, total)

    return roundOff(res)

