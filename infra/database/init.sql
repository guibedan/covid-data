\c covid-data;

CREATE TABLE regions (
    id CHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
    name varchar(255) NOT NULL UNIQUE,
    cases int NOT NULL,
    deaths int NOT NULL,
    population int NOT NULL,
    incidence DECIMAL(10,2) NOT NULL,
    mortality DECIMAL(10,2) NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE states (
    id CHAR(36) PRIMARY KEY DEFAULT (gen_random_uuid()),
    name varchar(255) NOT NULL UNIQUE,
    cases int NOT NULL,
    deaths int NOT NULL,
    population int NOT NULL,
    incidence DECIMAL(10,2) NOT NULL,
    mortality DECIMAL(10,2) NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cities (
    id CHAR(36) PRIMARY KEY DEFAULT (gen_random_uuid()),
    city varchar(255) NOT NULL,
    state CHAR(2) NOT NULL,
    city_ibge_code VARCHAR(7) NOT NULL,
    population INT NOT NULL,
    cases INT NOT NULL,
    deaths INT NOT NULL,
    incidence DECIMAL(10,4) NOT NULL,
    mortality DECIMAL(10,4) NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE world_countrys (
    id CHAR(36) PRIMARY KEY DEFAULT (gen_random_uuid()),
    name varchar(255) NOT NULL UNIQUE,
    cases int NOT NULL,
    deaths int NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);
