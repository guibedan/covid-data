from data.citys import city_request
from data.brazilData import request_regions_covid_data, request_states_covid_data
from data.worldData import world_request


def load():
    #city_request('./data/data_cities/table03.csv')
    request_regions_covid_data()
    request_states_covid_data()
    world_request()

