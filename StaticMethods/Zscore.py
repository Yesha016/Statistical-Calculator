from StaticMethods.division import division
from StaticMethods.roundOff import roundOff
from StaticMethods.subtraction import subtraction


def zscore(a, mean, sd):
    # TODO: Make an array loop to verify all values
    return roundOff(division(sd, subtraction(mean, a)))
