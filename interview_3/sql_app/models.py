from sqlalchemy import Column, String, Integer, Numeric

from .database import Base

class GPS (Base):

    __tablename__ = "cities"
    
    id = Column(Integer, primary_key=True)
    city = Column(String)
    area = Column(String)
    state = Column(String)
    latitude = Column(Numeric(17,15))
    longitude = Column(Numeric(17,15))