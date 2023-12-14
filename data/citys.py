import csv
from services.cities import CitiesService


def city_request(file_path):
    data_list = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(dict(row))

    CitiesService().add_cities(data_list)
