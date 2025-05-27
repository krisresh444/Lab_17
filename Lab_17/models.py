from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Label(Base): # Определяем модели таблиц
    __tablename__ = 'labels'

    label_id = Column(Integer, primary_key=True)
    label_name = Column(String)

    compositions = relationship("Composition", back_populates="label")

    def __repr__(self):
        return f"<Label(label_name='{self.label_name}')>"

class Composition(Base):
    __tablename__ = 'compositions'

    composition_id = Column(Integer, primary_key=True)
    title = Column(String)
    label_id = Column(Integer, ForeignKey('labels.label_id'))

    label = relationship("Label", back_populates="compositions")
    performances = relationship("Performance", back_populates="composition")

    def __repr__(self):
        return f"<Composition(title='{self.title}')>"

class Musician(Base):
    __tablename__ = 'musicians'

    musician_id = Column(Integer, primary_key=True)
    musician_name = Column(String)

    performances = relationship("Performance", back_populates="musician")

    def __repr__(self):
        return f"<Musician(musician_name='{self.musician_name}')>"

class Performance(Base):
    __tablename__ = 'performances'

    composition_id = Column(Integer, ForeignKey('compositions.composition_id'), primary_key=True)
    musician_id = Column(Integer, ForeignKey('musicians.musician_id'), primary_key=True)
    performance_date = Column(Date)

    composition = relationship("Composition", back_populates="performances")
    musician = relationship("Musician", back_populates="performances")

    def __repr__(self):
        return f"<Performance(composition_id={self.composition_id}, musician_id={self.musician_id})>"