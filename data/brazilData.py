import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from services.states import StatesService
from services.regions import RegionsService

options = Options()
options.add_argument('window-size=1920,1080')
options.add_argument('--headless')

url = 'https://covid.saude.gov.br'

nav = webdriver.Chrome(options=options)
nav.get(url)
region_tuple = ('Sul', 'Centro-Oeste', 'Norte', 'Nordeste', 'Sudeste', 'Brasil')


def take_data(start, end, states=True):
    covid_data = nav.find_elements(By.CSS_SELECTOR, '.lb-nome.lb-value')
    region_name = nav.find_elements(By.CSS_SELECTOR, '.lb-nome.nome-cit')

    data_dicts = []
    elements_per_set = 5

    for i in range(0, len(covid_data), elements_per_set):
        data_dict = {
            'name': region_name[i // elements_per_set].text,
            'cases': covid_data[i].text,
            'deaths': covid_data[i + 1].text,
            'incidence': covid_data[i + 2].text,
            'mortality': covid_data[i + 3].text,
        }

        data_dicts.append(data_dict)

    if states:
        format_data_dicts = [d for d in data_dicts if not d.get('name') in region_tuple]
        return format_data_dicts
    return data_dicts


def regions_request() -> None:
    time.sleep(10)

    close_tabs = ('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/div['
                  '1]/div/div[1]/lista-sanfona-component/div[3]/div[1]/div/div[1]/ion-button')
    nav.find_element(By.XPATH, close_tabs).click()

    data_dicts = take_data(None, None, False)

    RegionsService().add_regions(data_dicts)


def states_request() -> None:
    time.sleep(10)

    states_data = []

    sul = ('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/div['
           '1]/div/div[1]/lista-sanfona-component/div[3]/div[2]/div[1]/div[1]/ion-button')
    nav.find_element(By.XPATH, sul).click()
    states_data = states_data + take_data(2, 5)

    centro_oeste = ('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div'
                    '/div[1]/div/div[1]/lista-sanfona-component/div[3]/div[3]/div/div[1]/ion-button')
    nav.find_element(By.XPATH, centro_oeste).click()
    states_data = states_data + take_data(3, 7)

    norte = ('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/div['
             '1]/div/div[1]/lista-sanfona-component/div[3]/div[4]/div/div[1]/ion-button')
    nav.find_element(By.XPATH, norte).click()
    states_data = states_data + take_data(4, 11)

    nordeste = ('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/div['
                '1]/div/div[1]/lista-sanfona-component/div[3]/div[5]/div/div[1]/ion-button')
    nav.find_element(By.XPATH, nordeste).click()
    states_data = states_data + take_data(5, 14)

    sudeste = ('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/div['
               '1]/div/div[1]/lista-sanfona-component/div[3]/div[6]/div/div[1]/ion-button')
    nav.find_element(By.XPATH, sudeste).click()
    states_data = states_data + take_data(6, 10)

    StatesService().add_state(states_data)
