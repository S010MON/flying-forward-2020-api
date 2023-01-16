CREATE DATABASE IF NOT EXISTS auth;
USE auth;

CREATE TABLE users (
    id INT AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    hashed_password VARCHAR(255),
    disabled BOOLEAN,
    failed_attempts INT1,
    PRIMARY KEY (id)
    );

CREATE TABLE pilots (
    id INT AUTO_INCREMENT,
    ip VARCHAR(40),
    age INT(2),
    licenses VARCHAR(255),
    flight_hrs INT,
    PRIMARY KEY (id)
    );

CREATE TABLE missions (
    id INT AUTO_INCREMENT,
    pilot_id INT NOT NULL,
    success BOOLEAN,
    duration_secs INT,
    distance_m FLOAT,
    max_speed_mps FLOAT,
    avg_speed_mps FLOAT,
    max_height_m FLOAT,
    avg_height_m FLOAT,
    overflown_people INT,
    PRIMARY KEY (id),
    FOREIGN KEY (pilot_id) REFERENCES pilots(id)
    );