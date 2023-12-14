import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('window-size=1920,1080')
options.add_argument('--headless')

url = 'https://covid.saude.gov.br'

nav = webdriver.Chrome(options=options)
nav.get(url)


def request_regions_covid_data() -> list[dict]:
    time.sleep(10)

    colaps = ('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/div['
              '1]/div/div[1]/lista-sanfona-component/div[3]/div[1]/div/div[1]/ion-button')
    nav.find_element(By.XPATH, colaps).click()
    covid_data = nav.find_elements(By.CSS_SELECTOR, '.lb-nome.lb-value')
    region_name = nav.find_elements(By.CSS_SELECTOR, '.lb-nome.nome-cit')

    data_dicts = []
    elements_per_set = 5

    for i in range(0, len(covid_data), elements_per_set):
        data_dict = {
            'região': region_name[i // elements_per_set].text,
            'casos': covid_data[i].text,
            'Óbitos': covid_data[i + 1].text,
            'Incidência/100mil hab.': covid_data[i + 2].text,
            'Mortalidade/100mil hab': covid_data[i + 3].text,
            'Atualização': covid_data[i + 4].text
        }

        data_dicts.append(data_dict)

    return data_dicts


def take_data(start, end):
    covid_data = nav.find_elements(By.CSS_SELECTOR, '.lb-nome.lb-value')
    region_name = nav.find_elements(By.CSS_SELECTOR, '.lb-nome.nome-cit')

    data_dicts = []
    elements_per_set = 5

    for i in range(0, len(covid_data), elements_per_set):
        data_dict = {
            'estado': region_name[i // elements_per_set].text,
            'casos': covid_data[i].text,
            'Óbitos': covid_data[i + 1].text,
            'Incidência/100mil hab.': covid_data[i + 2].text,
            'Mortalidade/100mil hab': covid_data[i + 3].text,
            'Atualização': covid_data[i + 4].text
        }

        data_dicts.append(data_dict)

    return data_dicts[start:end]


def request_states_covid_data() -> list[dict]:
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

    return states_data
