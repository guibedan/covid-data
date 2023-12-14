from infra.postgres import PostgresDatabase
from uuid import uuid4


class RegionsRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def get_regions(self) -> list:
        query = """
            SELECT id, name, cases, deaths, incidence, mortality, updated_at FROM regions
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

    def add_regions(self, regions: dict) -> None:
        query = """
                INSERT INTO regions (id, name, cases, deaths, incidence, mortality)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

        self.db.execute(
            query,
            (
                str(uuid4()),
                regions["name"],
                regions["cases"],
                regions["deaths"],
                regions["incidence"],
                regions["mortality"]
            ),
        )
