
from pydantic import BaseModel


class JokeSchema(BaseModel):
    number: int | None = None
    text: str
  
