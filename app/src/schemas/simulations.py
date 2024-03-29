from pydantic import BaseModel


class PilotCreate(BaseModel):
    age: int
    licenses: str
    flight_hrs: int


class Pilot(PilotCreate):
    ip: str


class Mission(BaseModel):
    success: bool
    duration_secs: int
    distance_m: float
    max_speed_mps: float
    avg_speed_mps: float
    max_height_m: float
    avg_height_m: float
    overflown_people: int


class Simulation(BaseModel):
    pilot: PilotCreate
    mission: Mission

