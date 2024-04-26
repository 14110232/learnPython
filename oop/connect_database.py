import sqlite3

class ConnectDatabase:
  def __init__(self, db_name):
    self.con = sqlite3.connect(f"{db_name}")
    self.cur = self.con.cursor()

  def drop_table(self, table_name):
    self.cur.execute(f"DROP TABLE IF EXISTS {table_name};")

  def create_table(self, table_name, table_infos):
    sql = f"CREATE TABLE {table_name}("

    for key, value in table_infos.items():
      sql = sql + key + ' ' + value + ' NOT NULL,'

    self.cur.execute(f"""{sql[:-1]});""")

  def insert_multiple_rows(self, table_name, keys, new_data):
    self.cur.executemany(f"INSERT INTO {table_name}({keys}) values (?,?)", new_data)

  def verify_data(self, table_name):
    try:
      res = self.cur.execute(f"SELECT * FROM {table_name}")
      for item in res:
        print(f"{item[0]}: {item[1]}")
    except Exception as e:
      print(f"verify_data() => {e}")

  def close_connection(self):
    self.con.commit()
    self.con.close()