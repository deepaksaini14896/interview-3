from typing import List

from pydantic import BaseModel

class CityBase(BaseModel):
    city: str


class AreaCreate(CityBase):
    area: str


class StateCreate(AreaCreate):
    state: str
    
    class Config:
        orm_mode = True