from StaticMethods.Exceptions import exceptions
from StaticMethods.roundOff import roundOff


def division(a, b):
    error = exceptions(a, b)
    if error:
        result = float(b) / float(a)
        return roundOff(result)
    else:
        return 0
