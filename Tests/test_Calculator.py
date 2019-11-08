import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from StaticMethods.roundOff import roundOff


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        result = roundOff(4)
        self.assertEqual(self.calculator.add(2, 2), result)
        self.assertEqual(self.calculator.result, result)

    def test_add_method_calculatorCSV(self):
        test_data = CsvReader('Data/Addition.csv').data
        for row in test_data:
            result = roundOff(float(row['Result']))
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        result = roundOff(0)
        self.assertEqual(self.calculator.subtract(2, 2), result)
        self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculatorCSV(self):
        test_data = CsvReader('Data/Subtraction.csv').data
        for row in test_data:
            result = roundOff(float(row['Result']))
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        result = 4
        self.assertEqual(self.calculator.multiply(2, 2), result)
        self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculatorCSV(self):
        test_data = CsvReader('Data/Multiplication.csv').data
        for row in test_data:
            result = roundOff(float(row['Result']))
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        result = roundOff(2)
        self.assertEqual(self.calculator.divide(4, 8), result)
        self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculatorCSV(self):
        test_data = CsvReader('Data/Division.csv').data
        for row in test_data:
            result = roundOff((row['Result']))
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        result = roundOff(16)
        self.assertEqual(self.calculator.square(4), result)
        self.assertEqual(self.calculator.result, result)

    def test_square_method_calculatorCSV(self):
        test_data = CsvReader('Data/Square.csv').data
        for row in test_data:
            result = roundOff(float(row['Result']))
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt_method_calculator(self):
        result = roundOff(2)
        self.assertEqual(self.calculator.squareroot(4), result)
        self.assertEqual(self.calculator.result, result)

    def test_sqrt_method_calculatorCSV(self):
        test_data = CsvReader('Data/Square Root.csv').data
        for row in test_data:
            result = roundOff(float(row['Result']))
            self.assertAlmostEqual(self.calculator.squareroot(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()
