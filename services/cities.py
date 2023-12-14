from repository.cities import CitiesRepository

from marshmallow import ValidationError

from schemas.cities import AddCities


class CitiesService:
    def __init__(self):
        self.repository = CitiesRepository()

    def get_cities(self):
        return self.repository.get_cities()

    def add_cities(self, cities: list[dict]):
        #print(cities)
        try:
            for city in cities:
                AddCities().load(city)
                self.repository.add_cities(city)
        except ValidationError as err:
            return err.messages

        return 'success'
