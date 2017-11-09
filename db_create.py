import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
import json
import os
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Advertisement(Base):
    __tablename__ = 'advertisement'
    id = Column(Integer, primary_key=True)
    premise_area = Column(Float)
    rooms_number = Column(Integer)
    construction_year = Column(Integer)
    address = Column(String)
    has_balcony = Column(Boolean)
    living_area = Column(Float)
    oblast_district = Column(String)
    price = Column(Float)
    description = Column(String)
    under_construction = Column(Boolean)
    settlement = Column(String)


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def create():
    engine = create_engine(config.sqlalchemy_database_url, echo=True)
    Base.metadata.create_all(engine)
    advertisement_json = load_json_data('ads.json')
    Session = sessionmaker(bind=engine)
    session = Session()
    for ad in advertisement_json:
        session.add(Advertisement(**ad))
    session.commit()
