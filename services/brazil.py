from repository.cities import CitiesRepository
from repository.regions import RegionsRepository
from repository.states import StatesRepository

from data.regions_states import RegionsAndStatesData
from data.cities import CitiesData

from schemas.regions import AddRegions
from schemas.states import AddStates
from schemas.cities import AddCities

from marshmallow import ValidationError
import logging


class BrazilService:
    def __init__(self):
        self.cities_repository = CitiesRepository()
        self.regions_repository = RegionsRepository()
        self.states_repository = StatesRepository()

        self.regions_states_scrapper = RegionsAndStatesData()
        self.cities_scrapper = CitiesData()

    def get_top_cities(self) -> list:
        return self.cities_repository.get_top_cities()

    def get_cities(self, page: int = None) -> list:
        return self.cities_repository.get_cities(page)

    def add_cities(self) -> str:
        logging.info("Excetuing addCities Service")
        response = self.cities_scrapper.cities_request()

        logging.info("Validated an saving data on database")
        for _, row in response.iterrows():
            try:
                data_row = {
                    "city": row["city"],
                    "state": row["state"],
                    "city_ibge_code": str(int(row["city_ibge_code"])),
                    "population": int(row["estimated_population"]),
                    "cases": int(row["last_available_confirmed"]),
                    "deaths": int(row["last_available_deaths"]),
                    "incidence": float(row["last_available_confirmed_per_100k_inhabitants"]),
                    "mortality": float(row["last_available_death_rate"]),
                }
                AddCities().load(data_row)
                self.cities_repository.add_cities(data_row)
            except ValidationError as err:
                logging.error(err)

    def get_regions(self):
        return self.regions_repository.get_regions()

    def get_states(self):
        return self.states_repository.get_states()

    def save_states_and_regions(self):
        logging.info("Excetuing save_states_and_regions Service")
        return_data = self.regions_states_scrapper.regions_states_request()

        for region, data in return_data["regions"].items():
            save_data = data.copy()
            save_data["name"] = region

            try:
                AddRegions().load(save_data)
                self.regions_repository.add_regions(save_data)
            except ValidationError as err:
                logging.error(err)

        for name, state in return_data["states"].items():
            save_data = state.copy()
            save_data["name"] = name

            try:
                AddStates().load(save_data)
                self.states_repository.add_states(save_data)
            except ValidationError as err:
                logging.error(err)
