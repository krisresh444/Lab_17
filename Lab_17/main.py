from database import create_initial_data, get_db
from queries import run_queries
from models import Base
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///music.db'#движок SQLAlchemy
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
db_generator = get_db()
db = next(db_generator) 
create_initial_data(db)#заполняю базу данных
run_queries(db)#запросы
print("Завершено.")