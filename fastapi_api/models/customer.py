import datetime

from pydantic import BaseModel


class Customer(BaseModel):
    id: int = None
    name: str
    domain: str
    join_date: datetime.datetime = None
    is_active: bool
