from infra.postgres import PostgresDatabase
from uuid import uuid4


class StatesRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def get_states(self) -> list:
        query = """
            SELECT id, name, cases, deaths, incidence, mortality, updated_at FROM states
        """
        result = self.db.get(query)
        return list(
            map(
                lambda item: {
                    "id": item[0],
                    "name": item[1],
                    "cases": item[2],
                    "deaths": item[3],
                    "incidence": item[4],
                    "mortality": item[5],
                    "updated_at": item[6],
                },
                result,
            )
        )

    def add_states(self, state: dict) -> None:
        query = """
                INSERT INTO states (id, name, cases, deaths, incidence, mortality)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

        self.db.execute(
            query,
            (
                str(uuid4()),
                state["name"],
                state["cases"],
                state["deaths"],
                state["incidence"],
                state["mortality"]
            ),
        )
