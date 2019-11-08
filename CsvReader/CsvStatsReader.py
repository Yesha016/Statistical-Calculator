import csv
from collections import defaultdict


class CsvStatsReader:

    def __init__(self, filepath):
        self.columns = defaultdict(list)
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                for (k, v) in row.items():  # go over each column name and value
                    self.columns[k].append(v)
        pass
