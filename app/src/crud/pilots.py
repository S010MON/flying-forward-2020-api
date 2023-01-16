from sqlalchemy import update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.src.database.models import Pilot_db
from app.src.schemas.simulations import Pilot


def create_pilot(db: Session, pilot: Pilot) -> Pilot_db:

    db_pilot = Pilot_db(age=pilot.age,
                        licenses=pilot.licenses,
                        flight_hrs=pilot.flight_hrs,
                        ip=pilot.ip)
    db.add(db_pilot)
    db.commit()
    db.refresh(db_pilot)
    return db_pilot


def read_pilot(db: Session, ip: str) -> Pilot_db:
    return db.query(Pilot_db) \
        .filter(Pilot_db.ip == ip) \
        .first()
