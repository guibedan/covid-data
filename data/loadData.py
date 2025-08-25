from data.citys import city_request
from data.regions_states import regions_request, states_request
from data.worldData import world_request

from services.update import UpdateService


def load():
    print('Loading data...')
    regions_request()
    states_request()
    world_request()
    city_request('./data/data_cities/table03.csv')


def update():
    UpdateService().update()
    load()
