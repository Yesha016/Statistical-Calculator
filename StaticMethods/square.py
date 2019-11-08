from StaticMethods.Exceptions import exception


def square(a):
    error = exception(a)
    if error:
        result = float(a)*float(a)
        return result
    else:
        return 0
