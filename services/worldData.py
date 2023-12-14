import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def world_request():
    options = Options()
    options.add_argument('window-size=1920,1080')
    options.add_argument('--headless')

    url = 'https://covid19.who.int/table'

    nav = webdriver.Chrome(options=options)
    nav.get(url)

    time.sleep(1)

    nav.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[4]/div/div[2]/div/div/div[1]/div/div[1]/div/span[1]').click()
    div = nav.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[4]/div/div[2]/div/div/div[3]/div')
    all_country = []

    item_height = 50

    while True:

        names = nav.find_elements(By.CSS_SELECTOR, '.column_name.td')
        cases_total = nav.find_elements(By.CSS_SELECTOR, '.column_Cumulative_Confirmed.td')
        deaths_total = nav.find_elements(By.CSS_SELECTOR, '.column_Cumulative_Deaths.td')
        for i in range(len(names)):

            data_temp = {
                'name': names[i].text,
                'cases': cases_total[i].text,
                'deaths': deaths_total[i].text
            }

            if names[i].text == '+ By WHO Region' or names[i].text == '+ By World Bank Income Group':
                pass
            else:
                if data_temp not in all_country:
                    all_country.append(data_temp)

        nav.execute_script("arguments[0].scrollTop += {};".format(item_height * 25), div)
        time.sleep(1)

        if len(all_country) == 237:
            break

    return all_country
