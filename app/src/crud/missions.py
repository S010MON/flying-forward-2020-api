from typing import List

from sqlalchemy import update, select, join
from sqlalchemy.engine import Result, Row
from sqlalchemy.orm import Session
from app.src.database.models import Mission as Mission_in_db, Pilot as Pilot_in_db
from app.src.schemas.simulations import Mission


def create_mission(db: Session, mission: Mission, pilot: Pilot_in_db) -> Mission_in_db:
    db_mission = Mission_in_db(pilot_id=pilot.pilot_id,
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


def read_all_missions(db: Session) -> list[Row]:
    stmt = select(Mission_in_db.pilot_id,
                  Pilot_in_db.age,
                  Pilot_in_db.flight_hrs,
                  Pilot_in_db.licenses,
                  Mission_in_db.success,
                  Mission_in_db.duration_secs,
                  Mission_in_db.distance_m,
                  Mission_in_db.max_speed_mps,
                  Mission_in_db.avg_speed_mps,
                  Mission_in_db.max_height_m,
                  Mission_in_db.avg_height_m,
                  Mission_in_db.overflown_people,
                  ).join(Pilot_in_db, Mission_in_db.pilot_id == Pilot_in_db.pilot_id)
    return db.execute(stmt).fetchall()


def read_missions_by_pilot(db: Session, pilot_id: int) -> list[Row]:
    stmt = (select(Mission_in_db.pilot_id,
                   Pilot_in_db.age,
                   Pilot_in_db.flight_hrs,
                   Pilot_in_db.licenses,
                   Mission_in_db.success,
                   Mission_in_db.duration_secs,
                   Mission_in_db.distance_m,
                   Mission_in_db.max_speed_mps,
                   Mission_in_db.avg_speed_mps,
                   Mission_in_db.max_height_m,
                   Mission_in_db.avg_height_m,
                   Mission_in_db.overflown_people)
            .join(Pilot_in_db, Mission_in_db.pilot_id == Pilot_in_db.pilot_id)
            .where(Mission_in_db.pilot_id == pilot_id))
    return db.execute(stmt).fetchall()
