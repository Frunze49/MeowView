from sqlalchemy import Column, Integer, String, LargeBinary, ARRAY, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from django.contrib.postgres.fields import ArrayField
from django.db import models


Base = declarative_base()

class Statistics(Base):
    __tablename__ = 'statistics'
    id = Column(Integer, primary_key=True)
    author  = Column(String)
    post_id = Column(Integer)
    user_id = Column(Integer)
    like    = Column(BOOLEAN)
    view    = Column(BOOLEAN)

