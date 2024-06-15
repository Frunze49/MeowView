from sqlalchemy import Column, Integer, String, LargeBinary, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from django.contrib.postgres.fields import ArrayField
from django.db import models


Base = declarative_base()

class Statistics(Base):
    __tablename__ = 'statistics'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    user_like_ids = Column(ARRAY(Integer))
    user_view_ids = Column(ARRAY(Integer))

