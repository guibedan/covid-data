import io
import gzip
import logging
import requests
import pandas as pd


class CitiesData:
    def __init__(self):
        self.url = "https://data.brasil.io/dataset/covid19/caso_full.csv.gz"
        self.request = requests

    def cities_request(self) -> pd.DataFrame:
        logging.info("Init scrapping")

        response = self.request.get(self.url)
        csv_file = self.extract_file(response.content)

        df = pd.read_csv(io.BytesIO(csv_file), encoding="utf-8")

        df = df[df["place_type"] == "city"]
        df = df.sort_values(["city_ibge_code", "date"])
        latest = df.groupby("city_ibge_code").tail(1)

        result = latest[
            [
                "city",
                "state",
                "city_ibge_code",
                "estimated_population",
                "last_available_confirmed",
                "last_available_confirmed_per_100k_inhabitants",
                "last_available_deaths",
                "last_available_death_rate",
            ]
        ].reset_index(drop=True)

        return result

    def extract_file(self, content):
        with gzip.GzipFile(fileobj=io.BytesIO(content)) as gz:
            return gz.read()
