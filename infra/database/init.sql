\c Data_covid

CREATE TABLE regions (
    id CHAR(36) PRIMARY KEY DEFAULT UUID(),
    name varchar(255) NOT NULL UNIQUE,
    cases int NOT NULL,
    deaths int NOT NULL,
    population int NOT NULL,
    incidence DECIMAL(10,2) NOT NULL,
    mortality DECIMAL(10,2) NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE states (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    name varchar(255) NOT NULL UNIQUE,
    cases int NOT NULL,
    deaths int NOT NULL,
    population int NOT NULL,
    incidence DECIMAL(10,2) NOT NULL,
    mortality DECIMAL(10,2) NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE cities (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    name varchar(255) NOT NULL,
    state_id CHAR(36) NOT NULL,
    population int NOT NULL,
    incidence DECIMAL(10,2) NOT NULL,
    mortality DECIMAL(10,2) NOT NULL,
    type_region varchar(255) NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE world_countrys (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    name varchar(255) NOT NULL UNIQUE,
    cases int NOT NULL,
    deaths int NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

ALTER TABLE cities ADD CONSTRAINT fk_cities_1
FOREIGN KEY (state_id)
REFERENCES states (id);