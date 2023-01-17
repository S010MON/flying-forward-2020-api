from fastapi import APIRouter, Depends, HTTPException, status, Request

from sqlalchemy.orm import Session

from ..core.auth import oauth2_scheme
from ..crud.pilots import create_pilot, read_pilot
from ..crud.missions import create_mission
from ..schemas.simulations import Simulation, Pilot, Mission
from ..database.db_config import get_db

router = APIRouter(tags=['reports'])


@router.get("/report", status_code=status.HTTP_200_OK)
def generate_full_csv(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return {"Test": "Report"}
