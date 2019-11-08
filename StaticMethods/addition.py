from StaticMethods.Exceptions import exceptions
from StaticMethods.roundOff import roundOff


def addition(a, b):
    error = exceptions(a, b)
    if error:
        result = float(a) + float(b)
        return roundOff(result)
    else:
        return 0
