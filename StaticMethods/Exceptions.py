def exceptions(a, b):
    try:
        if a is None:
            raise ValueError
        if b is None:
            raise ValueError
    except ValueError:
        print("Please specify value a or b")
        return 0
    return 1

def exception(a):
    try:
        if a is None:
            raise ValueError
    except ValueError:
        print("Please specify value a or b")
        return 0
    return 1