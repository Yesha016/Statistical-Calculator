from StaticMethods.Exceptions import exceptions


def subtraction(a, b):
    error = exceptions(a, b)
    if error:
        result = float(b) - float(a)
        return result
    else:
        return 0
