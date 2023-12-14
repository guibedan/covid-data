from repository.regions import RegionsRepository

from marshmallow import ValidationError

from schemas.regions import AddRegions


class RegionsService:
    def __init__(self):
        self.repository = RegionsRepository()

    def get_regions(self):
        return self.repository.get_regions()

    def add_regions(self, regions: list[dict]):
        for region in regions:
            try:
                region["cases"] = int(remove_thousands_separator(region["cases"]))
                region["deaths"] = int(remove_thousands_separator(region["deaths"]))
                region["incidence"] = float(region["incidence"].replace(",", "."))
                region["mortality"] = float(region["mortality"].replace(",", "."))

                self.repository.add_regions(region)
            except ValueError as e:
                print(f"Erro ao adicionar a region {region['name']}: {e}")


def remove_thousands_separator(str_points):
    str_no_points = str_points.replace('.', '')
    return str_no_points
