from sqlalchemy.orm import Session
from sqlalchemy import text
import models
import schemas
from hash_pass import hash_password

from datetime import date, datetime

def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()

def create_user(db: Session, user: schemas.User):
    db_user = models.Product(login=user.login,
                             password=hash_password(user.password))
    db.add(db_user)
    db.commit()
