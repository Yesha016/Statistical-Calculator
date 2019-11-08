from StaticMethods.addition import addition
from StaticMethods.subtraction import subtraction
from StaticMethods.multiplication import multiplication
from StaticMethods.division import division
from StaticMethods.square import square
from StaticMethods.squareroot import squareroot

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction (a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = round(division(a, b), 9)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result

