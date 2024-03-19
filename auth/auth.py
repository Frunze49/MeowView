from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from crud import get_user_by_login, create_user
from database import SessionLocal, engine

from datetime import datetime
import re
from random import randint

from hash_pass import hash_password

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Роут для регистрации нового пользователя
@app.post("/register/")
def register_user(user: schemas.User, db: Session = Depends(get_db)):

    db_user = get_user_by_login(db, login=user.login)
    if db_user:
        raise HTTPException(status_code=409, detail="User already exits")

    create_user(db=db, user=user)
    return {"message": "Пользователь успешно зарегистрирован"}

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)