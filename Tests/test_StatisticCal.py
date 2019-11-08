import unittest

from CsvReader.CsvStatsReader import CsvStatsReader
from Statistics.StatisticCal import StatisticCal


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.stats = StatisticCal()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.stats, StatisticCal)

    def test_method_mean(self):
        row_data = CsvStatsReader('Data/Statistical_Data.csv')
        stats = row_data.columns['stats']
        mean = row_data.columns['mean'][0]
        self.assertEqual(self.stats.mean(stats), round(float(mean), 2) )


if __name__ == '__main__':
    unittest.main()
