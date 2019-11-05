import unittest

from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csvReader = CsvReader('Data/Addition.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.csvReader, CsvReader)


if __name__ == '__main__':
    unittest.main()
