from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from ..core.auth import oauth2_scheme
from ..crud.pilots import read_all_pilots, read_pilot_by_id
from ..crud.missions import read_all_missions, read_missions_by_pilot
from ..database.db_config import get_db

router = APIRouter(tags=['reports'])


@router.get("/report/missions", status_code=status.HTTP_200_OK)
async def get_all_missions(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    missions = read_all_missions(db)
    return missions


@router.get("/report/missions/csv", status_code=status.HTTP_200_OK)
async def get_all_missions_csv(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    missions = read_all_missions(db)
    print(str(missions[0]))
    with open("app/files/missions.csv", 'w') as file:
        file.write("pilot_id,age,flight_hrs,licenses,success,duration_secs,distance_m,max_speed_mps,avg_speed_mps,"
                   "max_height_m,avg_height_m,overflown_people\n")

        for i in range(len(missions)):
            file.write(f"{str(missions[i][0])},"
                       f"{str(missions[i][1])},"
                       f"{str(missions[i][2])},"
                       f"{str(missions[i][3])},"
                       f"{str(missions[i][4])},"
                       f"{str(missions[i][5])},"
                       f"{str(missions[i][6])},"
                       f"{str(missions[i][7])},"
                       f"{str(missions[i][8])},"
                       f"{str(missions[i][9])},"
                       f"{str(missions[i][10])},"
                       f"{str(missions[i][11])}\n")
    return FileResponse("app/files/missions.csv")


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
