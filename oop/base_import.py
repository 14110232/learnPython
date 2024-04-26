import connect_database
import csv
import operator
import re
import pdb

class BaseImport():
  def __init__(self):
    self.con = connect_database.ConnectDatabase('tutorial.db')
    self.model = self.model()

  def perform(self):
    self.con.drop_table(self.model.table_name)
    self.con.create_table(self.model.table_name, self.model.table_infos)

    new_rows = self.read_csv(self.model.CSV_PATH)
    keys = ', '.join(map(str, list(self.model.table_infos.keys())))

    try:
      self.con.insert_multiple_rows(self.model.table_name, keys, new_rows)
      self.con.verify_data(self.model.table_name)
    except Exception as e:
      pdb.set_trace()
      print("Error sqlite3")
    finally:
      self.con.close_connection()

  def read_csv(self, csv_path):
    with open(csv_path, encoding="utf8") as f:
      csv_reader = csv.reader(f)
      new_rows = sorted(csv_reader, key=operator.itemgetter(1))
    return new_rows

  def model(self):
    raise Exception("model not found")
