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


class Pilot_db(Base):
    __tablename__ = "pilots"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True, index=True)
    age = Column(Integer)
    licenses = Column(String)
    flight_hrs = Column(Integer)

    missions = relationship("Mission_db", back_populates="pilot")


class Mission_db(Base):
    __tablename__ = "missions"
    id = Column(Integer, primary_key=True, index=True)
    pilot_id = Column(ForeignKey("pilots.id"))

    success = Column(Boolean, default=False)
    duration_secs = Column(Integer)
    distance_m = Column(Float)
    max_speed_mps = Column(Float)
    avg_speed_mps = Column(Float)
    max_height_m = Column(Float)
    avg_height_m = Column(Float)
    overflown_people = Column(Integer)

    pilot = relationship("Pilot_db", back_populates="missions")
