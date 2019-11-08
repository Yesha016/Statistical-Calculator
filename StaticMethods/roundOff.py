from StaticMethods.Exceptions import exception


def roundOff(value):
    exception(value)
    return round(float(value), 2)
