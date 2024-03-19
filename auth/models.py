from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.orm import relationship

from database import Base


# Модель данных для пользователя
class User(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(DateTime(timezone=True))
    email = Column(String)
    phone = Column(String)

