from infra.postgres import PostgresDatabase


class UpdateRepository:
    def __init__(self):
        self.db = PostgresDatabase()
        self.db.get_connection()

    def update(self):
        self.db.execute(
            """
            DROP TABLE IF EXISTS cities;
            DROP TABLE IF EXISTS states;
            DROP TABLE IF EXISTS regions;
            DROP TABLE IF EXISTS world_countrys;
            """
        )

        self.db.execute(
            """
            CREATE TABLE regions (
                id CHAR(36) PRIMARY KEY,
                name varchar(255) NOT NULL,
                cases int NOT NULL,
                deaths int NOT NULL,
                incidence float NOT NULL,
                mortality float NOT NULL,
                created_at timestamp NOT NULL DEFAULT NOW(),
                updated_at timestamp NOT NULL DEFAULT NOW()
            );
            
            CREATE TABLE states (
                id CHAR(36) PRIMARY KEY,
                name varchar(255) NOT NULL,
                cases int NOT NULL,
                deaths int NOT NULL,
                incidence float NOT NULL,
                mortality float NOT NULL,
                created_at timestamp NOT NULL DEFAULT NOW(),
                updated_at timestamp NOT NULL DEFAULT NOW()
            );
            
            CREATE TABLE cities (
                id CHAR(36) PRIMARY KEY,
                name varchar(255) NOT NULL,
                state_id CHAR(36) NOT NULL,
                cases int NOT NULL,
                deaths int NOT NULL,
                type_region varchar(255) NOT NULL,
                created_at timestamp NOT NULL DEFAULT NOW(),
                updated_at timestamp NOT NULL DEFAULT NOW()
            );
            
            CREATE TABLE world_countrys (
                id CHAR(36) PRIMARY KEY,
                name varchar(255) NOT NULL,
                cases int NOT NULL,
                deaths int NOT NULL,
                created_at timestamp NOT NULL DEFAULT NOW(),
                updated_at timestamp NOT NULL DEFAULT NOW()
            );
            
            ALTER TABLE cities ADD CONSTRAINT fk_cities_1
            FOREIGN KEY (state_id)
            REFERENCES states (id);
            """
        )
