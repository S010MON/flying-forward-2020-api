from fastapi import APIRouter, Depends, HTTPException, status, Request

from sqlalchemy.orm import Session

from ..schemas.simulations import Simulation
from ..database.db_config import get_db

router = APIRouter(tags=['data'])


@router.post("/api/data/", status_code=status.HTTP_200_OK)
def post_simulation_data(simulation: Simulation,
                         request: Request,
                         db: Session = Depends(get_db)):
    print(request.client)
    print(simulation)
    return simulation
