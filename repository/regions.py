from infra.postgres import PostgresDatabase


class RegionsRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def get_regions(self) -> list:
        query = """
            SELECT id, name, cases, deaths, population, incidence, mortality, updated_at FROM regions
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

    def add_regions(self, regions: dict) -> None:
        query = """
                INSERT INTO regions (name, cases, deaths, population, incidence, mortality)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (name) DO UPDATE
                SET cases = EXCLUDED.cases,
                    deaths = EXCLUDED.deaths,
                    population = EXCLUDED.population,
                    incidence = EXCLUDED.incidence,
                    mortality = EXCLUDED.mortality;
            """

        self.db.execute(
            query,
            (
                regions["name"],
                regions["cases"],
                regions["deaths"],
                regions["population"],
                regions["incidence"],
                regions["mortality"]
            ),
        )
