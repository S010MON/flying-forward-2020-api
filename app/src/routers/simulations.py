from fastapi import APIRouter, Depends, HTTPException, status, Request

from sqlalchemy.orm import Session

from ..crud.pilots import create_pilot, read_pilot
from ..crud.missions import create_mission
from ..schemas.simulations import Simulation, Pilot
from ..database.db_config import get_db

router = APIRouter(tags=['data'])


@router.post("/api/data/", status_code=status.HTTP_200_OK)
def post_simulation_data(simulation: Simulation,
                         request: Request,
                         db: Session = Depends(get_db)):
    pilot = read_pilot(db, request.client.host)
    message = "pilot found in db"

    print(pilot.id, pilot.ip)

    if not pilot:
        message = "new pilot created"
        pilot_create = Pilot(age=simulation.pilot.age,
                             flight_hrs=simulation.pilot.flight_hrs,
                             licenses=simulation.pilot.licenses,
                             ip=request.client.host)
        pilot = create_pilot(db, pilot_create)

    simulation.mission
    mission = create_mission(db, simulation.mission, pilot)
    return {"message": message,
            "pilot": pilot.ip,
            "mission": mission}
