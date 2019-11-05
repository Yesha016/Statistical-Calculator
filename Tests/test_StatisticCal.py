import unittest

from Statistics.StatisticCal import StatisticCal


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.stats = StatisticCal()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.stats, StatisticCal)


if __name__ == '__main__':
    unittest.main()
