from StaticMethods.Exceptions import exception
from StaticMethods.roundOff import roundOff


def squareroot(a):
    error = exception(a)
    if error:
        result = float(a) ** 0.5
        return roundOff(result)
    else:
        return 0
