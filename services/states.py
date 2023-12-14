import re
from uuid import uuid4
from repository.states import StatesRepository
from marshmallow import ValidationError
from schemas.states import AddStates


class StatesService:
    def __init__(self):
        self.repository = StatesRepository()

    def get_states(self):
        return self.repository.get_states()

    def add_state(self, states: list[dict]):
        for state in states:
            try:
                state["cases"] = int(remove_thousands_separator(state["cases"]))
                state["deaths"] = int(remove_thousands_separator(state["deaths"]))
                state["incidence"] = float(state["incidence"].replace(",", "."))
                state["mortality"] = float(state["mortality"].replace(",", "."))

                AddStates().load(state)
                self.repository.add_states(state)
            except ValidationError as e:
                print(f"Erro ao adicionar o estado {state['name']}: {e}")


def remove_thousands_separator(str_points):
    str_no_points = str_points.replace('.', '')
    return str_no_points
