from infra.postgres import PostgresDatabase
from uuid import uuid4


class WorldRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def get_world(self) -> list:
        query = """
            SELECT name, cases, deaths, updated_at FROM world_countrys
        """
        result = self.db.get(query)
        return list(
            map(
                lambda item: {
                    "name": item[0],
                    "cases": item[1],
                    "deaths": item[2],
                    "updated_at": item[3],
                },
                result,
            )
        )

    def add_world(self, country: dict) -> None:
        query = """
            INSERT INTO world_countrys (id, name, cases, deaths)
            VALUES (%s, %s, %s, %s)
        """

        self.db.execute(
            query,
            (
                str(uuid4()),
                country["name"],
                country["cases"],
                country["deaths"]
            ),
        )
