import base_import
import city

class ImportCitiesService(base_import.BaseImport):
  def model(self):
    return city.City()
