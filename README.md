# Flying Forward 2020 Database and API

## Installation Guide

### Dependencies
Ensure that docker and docker-compose are installed

        docker version
        docker-compose --version
        
if not installed -> install ![docker](https://docs.docker.com/get-docker/) and ![docker-compose](https://docs.docker.com/compose/install/) for your OS


### Run Server
Navigate to the `flying-forward-2020-api/` root directory
        
Run the container:
        
        sudo docker-compose up

Done!

## API Specification 

### POST `/api/data` 
```json
{
  "pilot": {
    "age": int,
    "licenses": str,
    "flight_hrs": int,
  },
  "mission":
  {
    "success": boolean
    "duration_secs": int,
    "distance_m": float,
    "max_speed_mps": float,
    "avg_speed_mps": float,
    "max_height_m": float,
    "avg_height_m": float,
    "overflown_people": int,
  }
}
```

Example:
```json
{
  "pilot": {
    "age": 25,
    "licenses": "A1 & A3",
    "flight_hrs": 50
  },
  "mission":
  {
    "success": true,
    "duration_secs": 75,
    "distance_m": 1282.4,
    "max_speed_mps": 50.0,
    "avg_speed_mps": 32.1,
    "max_height_m": 200.0,
    "avg_height_m": 81.3,
    "overflown_people": 20
  }
}
```

#### Response:
None

## Database
### Users
```
+-------------------------------+--------------+------+-----+---------+----------------+
| Field                         | Type         | Null | Key | Default | Extra          |
+-------------------------------+--------------+------+-----+---------+----------------+
| user_id                       | int          | NO   | PRI | NULL    | auto_increment |
| username                      | varchar(255) | NO   |     | NULL    |                |
| hashed_password               | varchar(255) | NO   |     | NULL    |                |
+-------------------------------+--------------+------+-----+---------+----------------+
```
### Pilots
```bash
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| ip         | varchar(40)  | YES  |     | NULL    |                |
| age        | int          | YES  |     | NULL    |                |
| licenses   | varchar(255) | YES  |     | NULL    |                |
| flight_hrs | int          | YES  |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
```
### Missions
```bash
+------------------+------------+------+-----+---------+----------------+
| Field            | Type       | Null | Key | Default | Extra          |
+------------------+------------+------+-----+---------+----------------+
| id               | int        | NO   | PRI | NULL    | auto_increment |
| pilot_id         | int        | NO   | MUL | NULL    |                |
| success          | tinyint(1) | YES  |     | NULL    |                |
| duration_secs    | int        | YES  |     | NULL    |                |
| distance_m       | float      | YES  |     | NULL    |                |
| max_speed_mps    | float      | YES  |     | NULL    |                |
| avg_speed_mps    | float      | YES  |     | NULL    |                |
| max_height_m     | float      | YES  |     | NULL    |                |
| avg_height_m     | float      | YES  |     | NULL    |                |
| overflown_people | int        | YES  |     | NULL    |                |
+------------------+------------+------+-----+---------+----------------+
```
