from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from ..core.auth import oauth2_scheme
from ..crud.pilots import read_all_pilots, read_pilot_by_id
from ..crud.missions import read_all_missions, read_missions_by_pilot
from ..database.db_config import get_db

router = APIRouter(tags=['reports'])


@router.get("/report/missions", status_code=status.HTTP_200_OK)
def get_all_missions(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    missions = read_all_missions(db)
    return missions


@router.get("/report/missions/{pilot_id}", status_code=status.HTTP_200_OK)
async def get_missions_by_pilot(pilot_id: int,
                                db: Session = Depends(get_db),
                                token: str = Depends(oauth2_scheme)):
    pilot = read_pilot_by_id(db, pilot_id)
    if not pilot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    missions = read_missions_by_pilot(db, pilot_id)
    return missions


@router.get("/report/pilots", status_code=status.HTTP_200_OK)
async def get_all_pilots(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    pilots = read_all_pilots(db)
    return pilots
