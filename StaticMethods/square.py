from StaticMethods.Exceptions import exception
from StaticMethods.roundOff import roundOff


def square(a):
    error = exception(a)
    if error:
        result = float(a)*float(a)
        return roundOff(result)
    else:
        return 0
