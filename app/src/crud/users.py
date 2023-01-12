from sqlalchemy import update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.src.database import models
from app.src.schemas.users import User, UserCreate
from app.src.core import auth
from app.src.core.config import settings


def get_user(db: Session, username: str) -> User:
    return db.query(models.User)\
        .filter(models.User.username == username)\
        .first()


def create_user(db: Session, user: UserCreate):
    hashed_password = auth.hash_password(user.password)
    db_user = models.User(username=user.username,
                          hashed_password=hashed_password,
                          disabled=False)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_password(db: Session, user: UserCreate) -> bool:
    hashed_password = auth.hash_password(user.password)
    db.execute(update(models.User)
               .where(models.User.username == user.username)
               .values(hashed_password=hashed_password))
    try:
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False


def delete_user(db: Session, username: str) -> bool:
    user = db.query(models.User)\
        .filter(models.User.username == username)\
        .first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True


def increment_failed_attempts(db: Session, username):
    user = get_user(db, username)

    if user.failed_attempts > settings.MAX_PASSWORD_ATTEMTPS:
        set_user_disabled(db, username, True)

    db.execute(update(models.User)
               .where(models.User.username == username)
               .values(failed_attempts=(user.failed_attempts + 1)))
    try:
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False


def set_user_disabled(db: Session, username, disabled):
    db.execute(update(models.User)
               .where(models.User.username == username)
               .values(disabled=disabled))
    try:
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False
