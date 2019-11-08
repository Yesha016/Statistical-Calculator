from StaticMethods.Exceptions import exception


def squareroot(a):
    error = exception(a)
    if error:
        result = float(a) ** 0.5
        return result
    else:
        return 0
