from StaticMethods.Proportion import proportion
from StaticMethods.division import division
from StaticMethods.multiplication import multiplication
from StaticMethods.roundOff import roundOff
from StaticMethods.subtraction import subtraction


def varProportion(array, corr):
    n = len(array)
    prop = proportion(n, corr)
    res = division(n, multiplication(prop, subtraction(1, prop)))

    return roundOff(res)
