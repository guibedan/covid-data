import time
import os
import signal

from data.citys import city_request
from data.brazilData import regions_request, states_request
from data.worldData import world_request

from services.update import UpdateService


def load():
    print('Loading data...')
    regions_request()
    states_request()
    world_request()
    city_request('./data/data_cities/table03.csv')


def update():
    os.kill(os.getpid(), signal.SIGINT)
    UpdateService().update()
    load()
