import import_cities_service
import import_users_service

if __name__=="__main__":
  # cities
  object1 = import_cities_service.ImportCitiesService()
  object1.perform()

  # users
  object2 = import_users_service.ImportUsersService()
  object2.perform()
