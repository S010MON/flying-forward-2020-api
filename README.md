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
```
+-------------------------------+--------------+------+-----+---------+----------------+
| Field                         | Type         | Null | Key | Default | Extra          |
+-------------------------------+--------------+------+-----+---------+----------------+
| pilot_id                      | int          | NO   | PRI | NULL    | auto_increment |
| age                           | int          | YES  |     | NULL    |                |
| flying_minutes                | int          | YES  |     | NULL    |                |
| gender                        | varchar(1)   | YES  |     | NULL    |                |
| licences                      | varchar(255) | YES  |     | NULL    |                |
| map                           | varchar(255) | YES  |     | NULL    |                |
| time_overflying_people_ms     | int          | YES  |     | NULL    |                |
| number_overflown_people       | int          | YES  |     | NULL    |                |
| min_dist_to_nearest_structure | double       | YES  |     | NULL    |                |
| min_dist_to_nearest_person    | double       | YES  |     | NULL    |                |
| avg_dist_to_intruder          | double       | YES  |     | NULL    |                |
| max_dist_to_start             | double       | YES  |     | NULL    |                |
| gated_vul_points              | int          | YES  |     | NULL    |                |
+-------------------------------+--------------+------+-----+---------+----------------+
```
