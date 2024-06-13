from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создайте движок для подключения к базе данных
engine = create_engine('postgresql://postgres:postgres@postgresql/statistic_database') # temp

# Создайте фабрику сессий
Session = sessionmaker(bind=engine)
