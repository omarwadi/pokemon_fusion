from pydantic import BaseModel

class Pokemon(BaseModel):
    type1: str
    type2: str | None = None
    pokemon1: str
    pokemon2: str | None = None
    description: str
