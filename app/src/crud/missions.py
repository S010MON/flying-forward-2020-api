from sqlalchemy import update, select, join
from sqlalchemy.orm import Session
from app.src.database.models import Mission_db, Pilot_db
from app.src.schemas.simulations import Mission


def create_mission(db: Session, mission: Mission, pilot: Pilot_db):
    db_mission = Mission_db(pilot_id=pilot.id,
                            success=mission.success,
                            duration_secs=mission.duration_secs,
                            distance_m=mission.distance_m,
                            max_speed_mps=mission.max_speed_mps,
                            avg_speed_mps=mission.avg_speed_mps,
                            max_height_m=mission.max_height_m,
                            avg_height_m=mission.avg_height_m,
                            overflown_people=mission.overflown_people)
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


def read_missions(db: Session, ip: str) -> Pilot_db:
    stmt = select(Mission_db).join(Pilot_db)
    return db.execute(stmt)
