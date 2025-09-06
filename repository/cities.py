from infra.postgres import PostgresDatabase


class CitiesRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def get_cities(self, page: int) -> list:
        query = """
            SELECT city, state, city_ibge_code, population, cases, deaths, incidence, mortality, updated_at
            FROM cities
            ORDER BY city, state ASC
        """

        if page:
            query += f"""
                LIMIT 10 OFFSET {10*(page-1)}
            """

        result = self.db.get(query)
        return list(
            map(
                lambda item: {
                    "city": item[0],
                    "state": item[1],
                    "city_ibge_code": item[2],
                    "population": item[3],
                    "cases": item[4],
                    "deaths": item[5],
                    "incidence": item[6],
                    "mortality": item[7],
                    "updated_at": item[8]
                },
                result,
            )
        )

    def get_top_cities(self) -> list:
        query = """
            SELECT city, state, city_ibge_code, population, cases, deaths, incidence, mortality, updated_at
            FROM cities
            ORDER BY cases DESC
            LIMIT 10
        """

        result = self.db.get(query)
        return list(
            map(
                lambda item: {
                    "city": item[0],
                    "state": item[1],
                    "city_ibge_code": item[2],
                    "population": item[3],
                    "cases": item[4],
                    "deaths": item[5],
                    "incidence": item[6],
                    "mortality": item[7],
                    "updated_at": item[8]
                },
                result,
            )
        )

    def add_cities(self, city: dict) -> None:
        query = """
            INSERT INTO cities (
                city, state, city_ibge_code, population, cases, deaths, incidence, mortality
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s
            )
            ON CONFLICT (city_ibge_code) DO UPDATE
            SET population = EXCLUDED.population,
                cases = EXCLUDED.cases,
                deaths = EXCLUDED.deaths,
                incidence = EXCLUDED.incidence,
                mortality = EXCLUDED.mortality,
                updated_at = CURRENT_TIMESTAMP;
        """

        self.db.execute(
            query,
            (
                city["city"],
                city["state"],
                city["city_ibge_code"],
                city["population"],
                city["cases"],
                city["deaths"],
                city["incidence"],
                city["mortality"]
            ),
        )
