import logging
from requests import Session


class RegionsAndStatesData:
    def __init__(self):
        self.session = Session()
        self.urls_per_regions = {
            'sudeste': 'https://qd28tcd6b5.execute-api.sa-east-1.amazonaws.com/prod/PortalSinteseSepUfSudeste',
            'sul': 'https://qd28tcd6b5.execute-api.sa-east-1.amazonaws.com/prod/PortalSinteseSepUfSul',
            'centro_oeste': 'https://qd28tcd6b5.execute-api.sa-east-1.amazonaws.com/prod/PortalSinteseSepUfCentroOeste',
            'norte': 'https://qd28tcd6b5.execute-api.sa-east-1.amazonaws.com/prod/PortalSinteseSepUfNorte',
            'nordeste': 'https://qd28tcd6b5.execute-api.sa-east-1.amazonaws.com/prod/PortalSinteseSepUfNordeste',
        }

    def regions_states_request(self):
        return_data = {"regions": {}, "states": {}}

        for region, url in self.urls_per_regions.items():
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            resp_json = response.json()

            if not resp_json or not isinstance(resp_json, list):
                logging.warning(f"Unexpected response format for {region}")
                continue

            region_data = {"casosAcumulado": 0, "obitosAcumulado": 0, "populacaoTCU2019": 0}
            for state in resp_json:
                state_stats = self.calculate_statistics(state)
                return_data["states"][state["_id"]] = state_stats

                region_data["casosAcumulado"] += state_stats["cases"]
                region_data["obitosAcumulado"] += state_stats["deaths"]
                region_data["populacaoTCU2019"] += state_stats["population"]

            return_data["regions"][region] = self.calculate_statistics(region_data)
        return return_data

    def calculate_statistics(self, data):
        return {
            "cases": data["casosAcumulado"],
            "deaths": data["obitosAcumulado"],
            "population": data["populacaoTCU2019"],
            "incidence": self.calculate_percent(data["casosAcumulado"], data["populacaoTCU2019"]),
            "mortality": self.calculate_percent(data["obitosAcumulado"], data["populacaoTCU2019"]),
        }

    def calculate_percent(self, pivot, population):
        return round((pivot / population) * 100000, 2) if population > 0 else 0.00
