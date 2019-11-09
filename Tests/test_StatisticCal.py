import unittest

from CsvReader.CsvStatsReader import CsvStatsReader
from StaticMethods.roundOff import roundOff
from Statistics.StatisticCal import StatisticCal


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.stats = StatisticCal()
        self.row_data = CsvStatsReader('Data/Statistical_Data.csv')
        self.stats_row = self.row_data.columns['stats']

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.stats, StatisticCal)

    def test_method_mean(self):
        mean = roundOff(float(self.row_data.columns['mean'][0]))
        self.assertEqual(self.stats.mean(self.stats_row), mean)
        self.assertEqual(self.stats.result, mean)

    def test_method_median(self):
        median = roundOff(float(self.row_data.columns['median'][0]))
        self.assertEqual(self.stats.median(self.stats_row), median)
        self.assertEqual(self.stats.result, median)

    def test_method_mode(self):
        mode = roundOff(float(self.row_data.columns['mode'][0]))
        self.assertEqual(self.stats.mode(self.stats_row), mode)
        self.assertEqual(self.stats.result, mode)

    def test_method_sd(self):
        sd = round(float(self.row_data.columns['sd'][0]), 2)
        self.assertEqual(self.stats.sd(self.stats_row), sd)
        self.assertEqual(self.stats.result, sd)

    def test_method_vpp(self):
        vpp = round(float(self.row_data.columns['vpp'][0]), 2)
        self.assertEqual(self.stats.vpp(self.stats_row), vpp)
        self.assertEqual(self.stats.result, vpp)

    def test_method_zscore(self):
        mean = self.row_data.columns['mean'][0]
        sd = self.row_data.columns['sd'][0]
        zscore = roundOff(self.row_data.columns['zscore'][0])

        # zscore = roundOff(float(row['zscore']))
        self.assertEqual(self.stats.zscore(self.stats_row[0], mean, sd), zscore)
        self.assertEqual(self.stats.result, zscore)

if __name__ == '__main__':
    unittest.main()
