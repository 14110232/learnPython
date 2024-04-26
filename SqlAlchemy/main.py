import city

if __name__=="__main__":
  object = city.City()
  object.create_table()
  object.import_rows()
  object.show()