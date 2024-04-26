import base_import
import user

class ImportUsersService(base_import.BaseImport):
  def model(self):
    return user.User()
