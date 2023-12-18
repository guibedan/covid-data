from repository.cities import CitiesRepository

from marshmallow import ValidationError

from schemas.cities import AddCities


class CitiesService:
    def __init__(self):
        self.repository = CitiesRepository()

    def get_cities(self):
        return self.repository.get_cities()

    def add_cities(self, cities: list[dict]):
        try:
            for city in cities:
                city["CasosAcumulados"] = int(city["CasosAcumulados"].replace(".", ""))
                city["ObitosAcumulados"] = int(city["ObitosAcumulados"].replace(".", ""))

                data_city = {
                    'name': city['Município'],
                    'state_id': city['UF'],
                    'cases': city['CasosAcumulados'],
                    'deaths': city['ObitosAcumulados'],
                    'type_region': city['Metro/Interior']
                }

                #AddCities().load(city)
                self.repository.add_cities(data_city)
        except ValidationError as err:
            return err.messages

        return 'success'
