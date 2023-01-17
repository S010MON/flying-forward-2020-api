from fastapi import APIRouter, Depends, HTTPException, status, Request

from sqlalchemy.orm import Session

from ..crud.pilots import create_pilot, read_pilot_by_ip
from ..crud.missions import create_mission
from ..schemas.simulations import Simulation, Pilot
from ..database.db_config import get_db

router = APIRouter(tags=['data'])


@router.post("/api/data/", status_code=status.HTTP_200_OK)
async def post_simulation_data(simulation: Simulation,
                               request: Request,
                               db: Session = Depends(get_db)):
    validate_input(simulation)

    try:
        pilot_ip = request.headers["x-forwarded-for"]
    except KeyError:
        pilot_ip = request.client.host

    pilot = read_pilot_by_ip(db, pilot_ip)
    message = f"pilot found in db {pilot_ip}"

    if not pilot:
        message = f"new pilot created {pilot_ip}"
        pilot_create = Pilot(age=simulation.pilot.age,
                             flight_hrs=simulation.pilot.flight_hrs,
                             licenses=simulation.pilot.licenses,
                             ip=request.client.host)
        pilot = create_pilot(db, pilot_create)

    create_mission(db, simulation.mission, pilot)
    return {"message": message}


def validate_input(simulation: Simulation) -> bool:
    age = simulation.pilot.age
    if age < 0 or age > 99:
        raise HTTPException(status_code=400,
                            detail="Invalid age entered")

    if simulation.pilot.flight_hrs < 0:
        raise HTTPException(status_code=400,
                            detail="Invalid flight experience entered")

    if len(simulation.pilot.licenses) > 255:
        raise HTTPException(status_code=400,
                            detail="Too many chars entered for licence")
