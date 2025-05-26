from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Boolean
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///habit_tracker.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Habit(Base):
    __tablename__ = 'habit'
    id = Column(Integer, primary_key=True)
    habit_name = Column(String)
    frequency = Column(String)
    is_done = Column(Boolean)
    habit_streak = Column(Integer)
    logs = relationship('HabitLog', back_populates='habit')

class HabitLog(Base):
    __tablename__ = 'habit_log'
    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey('habit.id'))
    date_logged = Column(String)
    habit = relationship('Habit', back_populates='logs')

Base.metadata.create_all(engine)
