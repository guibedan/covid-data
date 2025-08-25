from infra.postgres import PostgresDatabase


class StatesRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def get_states(self) -> list:
        query = """
            SELECT id, name, cases, deaths, population, incidence, mortality, updated_at FROM states
        """
        result = self.db.get(query)
        return list(
            map(
                lambda item: {
                    "id": item[0],
                    "name": item[1],
                    "cases": item[2],
                    "deaths": item[3],
                    "population": item[4],
                    "incidence": item[5],
                    "mortality": item[6],
                    "updated_at": item[7],
                },
                result,
            )
        )

    def add_states(self, state: dict) -> None:
        query = """
                INSERT INTO states (name, cases, deaths, population, incidence, mortality)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                name=%s, cases=%s, deaths=%s, population=%s, incidence=%s, mortality=%s
            """

        self.db.execute(
            query,
            (
                state["name"],
                state["cases"],
                state["deaths"],
                state["population"],
                state["incidence"],
                state["mortality"]
            ),
        )
