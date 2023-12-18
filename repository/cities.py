from infra.postgres import PostgresDatabase
from uuid import uuid4


class CitiesRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def get_cities(self) -> list:
        query = """
            SELECT cities.name AS city_name, cities.cases, cities.deaths, states.name AS state_name, cities.type_region, cities.updated_at 
            FROM cities
            INNER JOIN states ON cities.state_id = states.id;
        """
        result = self.db.get(query)
        return list(
            map(
                lambda item: {
                    "name": item[0],
                    "cases": item[1],
                    "deaths": item[2],
                    "UF": item[3],
                    "type_region": item[4],
                    "updated_at": item[5]
                },
                result,
            )
        )

    def add_cities(self, city: dict) -> None:
        query = """
            INSERT INTO cities (id, name, state_id, cases, deaths, type_region)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        state = self.db.get("""
                                SELECT id FROM states WHERE name = %s
                            """,
                            (str(city["state_id"]),), )

        self.db.execute(
            query,
            (
                str(uuid4()),
                city["name"],
                str(state[0][0]),
                city["cases"],
                city["deaths"],
                city["type_region"]
            ),
        )
