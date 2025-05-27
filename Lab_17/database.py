from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Label, Composition, Musician, Performance
from datetime import date

DATABASE_URL = 'sqlite:///music.db'

engine = create_engine(DATABASE_URL)#создаем движок SQLAlchemy 

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#создаем сессию для работы с БД

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_initial_data(db):
    #лейбы
    label1 = Label(label_name="Columbia Records")
    label2 = Label(label_name="Def Jam Recordings")
    label3 = Label(label_name="Motown")
    #композиции
    composition1 = Composition(title="Bohemian Rhapsody", label=label1)
    composition2 = Composition(title="Hallelujah", label=label1)
    composition3 = Composition(title="Numb", label=label2)
    composition4 = Composition(title="Superstition", label=label3)
    #музыканты
    musician1 = Musician(musician_name="Queen")
    musician2 = Musician(musician_name="Jeff Buckley")
    musician3 = Musician(musician_name="Linkin Park")
    musician4 = Musician(musician_name="Stevie Wonder")
    musician5 = Musician(musician_name="Beyonce")
    #выступления
    performance1 = Performance(composition=composition1, musician=musician1, performance_date=date(1975, 10, 31))
    performance2 = Performance(composition=composition2, musician=musician2, performance_date=date(1994, 8, 28))
    performance3 = Performance(composition=composition3, musician=musician3, performance_date=date(2003, 3, 25))
    performance4 = Performance(composition=composition4, musician=musician4, performance_date=date(1972, 10, 24))
    performance5 = Performance(composition=composition1, musician=musician5, performance_date=date(2018, 9, 5)) 

    db.add_all([label1, label2, label3, composition1, composition2, composition3, composition4, musician1, musician2, musician3, musician4, musician5, performance1, performance2, performance3, performance4, performance5])

    db.commit() #фиксируем изменения в БД
    print("База данных заполнена.")