import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def request_brazil_covid_data() -> list[dict[str, str]]:
    options = Options()
    options.add_argument('window-size=1920,1080')
    options.add_argument('--headless')

    url = 'https://covid.saude.gov.br'

    nav = webdriver.Chrome(options=options)
    nav.get(url)

    time.sleep(20)

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
