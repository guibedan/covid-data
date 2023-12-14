from repository.world import WorldRepository

from marshmallow import ValidationError

from schemas.world import AddWorld


class WorldService:
    def __init__(self):
        self.repository = WorldRepository()

    def get_world(self):
        return self.repository.get_world()

    def add_world(self, world: list[dict]):
        try:
            for e in world:
                cases_value = e["cases"].replace(",", "")
                e["cases"] = int(cases_value) if cases_value else 0
                deaths_value = e["deaths"].replace(",", "")
                e["deaths"] = int(deaths_value) if deaths_value else 0
                AddWorld().load(e)
                self.repository.add_world(e)
        except ValidationError as err:
            return err.messages

        return 'success'
