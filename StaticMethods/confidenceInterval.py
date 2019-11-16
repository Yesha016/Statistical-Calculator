from StaticMethods.CalulcateMean import calMean
from StaticMethods.PopulationStandardDeviation import stddev
from StaticMethods.addition import addition
from StaticMethods.division import division
from StaticMethods.multiplication import multiplication
from StaticMethods.roundOff import roundOff
from StaticMethods.squareroot import squareroot
from StaticMethods.subtraction import subtraction


def confidenceInterval(array, conf):

    n = squareroot(len(array))
    mean = calMean(array)
    sd = stddev(array)
    if conf == 80:
        t = 1.282
    elif conf == 85:
        t = 1.440
    elif conf == 90:
        t = 1.645
    elif conf == 95:
        t = 1.960
    else:  # 99.5 default confidence percentage
        t = 2.807

    ciLower = subtraction(multiplication(division(n, sd), t), mean)
    ciUpper = addition(mean, multiplication(division(n, sd), t))
    return roundOff(ciLower), roundOff(ciUpper)
