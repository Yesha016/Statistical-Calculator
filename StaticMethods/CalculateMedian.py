from StaticMethods.Exceptions import exception


def calMedian(a):
    length = len(a)
    half = int(length / 2)

    for val in a:
        exception(val)

    if length % 2 == 0:
        median = float(float(a[half - 1]) + float(a[half])) / 2
    else:
        median = a[half]

    return round(float(median), 2)
