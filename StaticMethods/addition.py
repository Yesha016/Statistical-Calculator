from StaticMethods.Exceptions import exceptions


def addition(a, b):
    error = exceptions(a, b)
    if error:
        result = float(a) + float(b)
        return result
    else:
        return 0
