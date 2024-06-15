from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создайте движок для подключения к базе данных
engine = create_engine('postgresql://postgres:postgres@postgresql/posts_database') # temp

# Создайте фабрику сессий
PostSession = sessionmaker(bind=engine)
