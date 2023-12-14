from infra.postgres import PostgresDatabase
from uuid import uuid4


class CitiesRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def get_cities(self) -> list:
        query = """
            SELECT name, cases, deaths, updated_at FROM cities
        """
        result = self.db.get(query)
        return list(
            map(
                lambda item: {
                    "name": item[0],
                    "cases": item[1],
                    "deaths": item[2],
                    "updated_at": item[3]
                },
                result,
            )
        )

    def add_cities(self, cities: dict) -> None:

        query = """
            INSERT INTO cities (id, name, state_id, cases, deaths)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        for city in cities:
            state = self.db.get("""
                                SELECT id FROM states WHERE name = %s
                            """,
                                (str(city["UF"]),),)

            print(state)

            self.db.execute(
                query,
                (
                    str(uuid4()),
                    city["Município"],
                    str(state[0]),
                    city["CasosAcumulados"],
                    city["ObitosAcumulados"]
                ),
            )