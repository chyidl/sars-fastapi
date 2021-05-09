from datetime import date
from pydantic import BaseModel


class Record(BaseModel):
    id: int
    date: date
    country: str
    cases: int
    deaths: int
    recoveries: int

    class Config:
        # allows the app to take ORM objects and translate them into responses automatically. This automation saves us from manually taking data out of ORM, making it into a dictionary, the loading it in with Pydantic
        orm_mode = True
