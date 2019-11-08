import unittest

from CsvReader.CsvStatsReader import CsvStatsReader
from Statistics.StatisticCal import StatisticCal


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.stats = StatisticCal()
        self.row_data = CsvStatsReader('Data/Statistical_Data.csv')
        self.stats_row = self.row_data.columns['stats']

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.stats, StatisticCal)

    def test_method_mean(self):
        mean = round(float(self.row_data.columns['mean'][0]), 2)
        self.assertEqual(self.stats.mean(self.stats_row), mean)
        self.assertEqual(self.stats.result, mean)

    def test_method_median(self):
        median = round(float(self.row_data.columns['median'][0]), 2)
        self.assertEqual(self.stats.median(self.stats_row), median)
        self.assertEqual(self.stats.result, median)

    def test_method_sd(self):
        sd = round(float(self.row_data.columns['sd'][0]), 2)
        self.assertEqual(self.stats.sd(self.stats_row), sd)
        self.assertEqual(self.stats.result, sd)

    def test_method_vpp(self):
        vpp = round(float(self.row_data.columns['vpp'][0]), 2)
        self.assertEqual(self.stats.vpp(self.stats_row), vpp)
        self.assertEqual(self.stats.result, vpp)




if __name__ == '__main__':
    unittest.main()
