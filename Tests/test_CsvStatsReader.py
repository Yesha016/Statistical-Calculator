import unittest

from CsvReader.CsvStatsReader import CsvStatsReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csvStatsReader = CsvStatsReader('Data/Statistical_Data.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.csvStatsReader, CsvStatsReader)


if __name__ == '__main__':
    unittest.main()
