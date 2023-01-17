from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database.db_config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
    failed_attempts = Column(Integer, default=0)


class Pilot(Base):
    __tablename__ = "pilots"
    pilot_id = Column(Integer, primary_key=True)
    ip = Column(String, unique=True)
    age = Column(Integer)
    licenses = Column(String)
    flight_hrs = Column(Integer)

    missions = relationship("Mission")


class Mission(Base):
    __tablename__ = "missions"
    mission_id = Column(Integer, primary_key=True)

    success = Column(Boolean, default=False)
    duration_secs = Column(Integer)
    distance_m = Column(Float)
    max_speed_mps = Column(Float)
    avg_speed_mps = Column(Float)
    max_height_m = Column(Float)
    avg_height_m = Column(Float)
    overflown_people = Column(Integer)

    pilot_id = Column(Integer, ForeignKey("pilots.pilot_id"))
    pilot = relationship("Pilot", back_populates="missions")
