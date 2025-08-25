from repository.cities import CitiesRepository
from repository.regions import RegionsRepository
from repository.states import StatesRepository

from data.regions_states import RegionsAndStatesData

from schemas.regions import AddRegions
from schemas.states import AddStates

from marshmallow import ValidationError
import logging


class BrazilService:
    def __init__(self):
        self.cities_repository = CitiesRepository()
        self.regions_repository = RegionsRepository()
        self.states_repository = StatesRepository()

        self.regions_states_scrapper = RegionsAndStatesData()
        self.cities_scrapper = RegionsAndStatesData()

    def get_cities(self, page: int = None) -> list:
        return self.cities_repository.get_cities(page)

    def add_cities(self, cities: list[dict]) -> str:
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

    def get_regions(self):
        return self.regions_repository.get_regions()
    
    def get_states(self):
        return self.states_repository.get_states()

    def save_states_and_regions(self):
        return_data = self.regions_states_scrapper.regions_states_request()

        for region, data in return_data["regions"].items():
            save_data = data.copy()
            save_data["name"] = region

            try:
                AddRegions(save_data)
                self.regions_repository.add_regions(save_data)
            except ValidationError as err:
                logging.error(err)

        for state in return_data["states"].items():
            save_data = data.copy()
            save_data["name"] = state

            try:
                AddStates(save_data)
                self.states_repository.add_states(save_data)
            except ValidationError as err:
                logging.error(err)
