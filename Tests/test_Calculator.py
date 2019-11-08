import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        calculator = Calculator()
        result = 4
        self.assertEqual(calculator.add(2, 2), result)
        self.assertEqual(calculator.result, result)

    def test_add_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(calculator.result, result)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        result = 0
        self.assertEqual(calculator.subtract(2, 2), result)
        self.assertEqual(calculator.result, result)

    def test_subtract_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(calculator.result, result)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        result = 4
        self.assertEqual(calculator.multiply(2, 2), result)
        self.assertEqual(calculator.result, result)

    def test_multiply_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(calculator.result, result)

    def test_divide_method_calculator(self):
        calculator = Calculator()
        result = 2
        self.assertEqual(calculator.divide(4, 8), result)
        self.assertEqual(calculator.result, result)

    def test_divide_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(calculator.result, result)

    def test_square_method_calculator(self):
        calculator = Calculator()
        result = 16
        self.assertEqual(calculator.square(4), result)
        self.assertEqual(calculator.result, result)

    def test_square_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(calculator.square(row['Value 1']), result)
            self.assertEqual(calculator.result, result)

    def test_sqrt_method_calculator(self):
        calculator = Calculator()
        result = 2
        self.assertEqual(calculator.squareroot(4), result)
        self.assertEqual(calculator.result, result)

    def test_sqrt_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Square Root.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(calculator.squareroot(row['Value 1']), result)
            self.assertAlmostEqual(calculator.result, result)


if __name__ == '__main__':
    unittest.main()
