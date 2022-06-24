
from pydantic import BaseModel


class Joke(BaseModel):
    title: str
    value: str 
