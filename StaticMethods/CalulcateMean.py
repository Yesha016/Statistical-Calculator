from StaticMethods.Exceptions import exception


def calMean(a):
    total = 0
    for val in a:
        exception(a)
        total += float(val)

    return round(float(total / len(a)), 2)
