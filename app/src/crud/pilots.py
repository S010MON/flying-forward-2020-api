from sqlalchemy import select
from sqlalchemy.orm import Session
from app.src.database.models import Pilot as Pilot_in_db
from app.src.schemas.simulations import Pilot


def create_pilot(db: Session, pilot: Pilot) -> Pilot_in_db:
    db_pilot = Pilot_in_db(age=pilot.age,
                           licenses=pilot.licenses,
                           flight_hrs=pilot.flight_hrs,
                           ip=pilot.ip)
    db.add(db_pilot)
    db.commit()
    db.refresh(db_pilot)
    return db_pilot


def read_pilot_by_ip(db: Session, ip: str) -> Pilot_in_db:
    return db.query(Pilot_in_db) \
        .filter(Pilot_in_db.ip == ip) \
        .first()


def read_pilot_by_id(db: Session, id: int) -> Pilot_in_db:
    return db.query(Pilot_in_db) \
        .filter(Pilot_in_db.pilot_id == id) \
        .first()


def read_all_pilots(db: Session) -> list:
    stmt = select(Pilot_in_db)
    return db.execute(stmt).fetchall()
