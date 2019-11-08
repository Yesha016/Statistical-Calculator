from StaticMethods.addition import addition


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        # a = input("Enter value for a: ")
        # b = input("Enter value for b: ")
        try:
            if a is None:
                raise ValueError
            if b is None:
                raise ValueError
            self.result = addition(int(a), int(b))
            return self.result
        except ValueError:
            print("Please specify value a or b")
