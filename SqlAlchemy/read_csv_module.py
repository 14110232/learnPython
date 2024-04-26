import csv
import operator

def read_csv(csv_path):
  with open(csv_path, encoding="utf8") as f:
    csv_reader = csv.reader(f)
    new_rows = sorted(csv_reader, key=operator.itemgetter(1))
  return new_rows