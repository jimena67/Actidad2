from typing import List, Dict
from datetime import date

from pydantic import BaseModel

# Declaras la variable como un str
# y obtienes soporte del editor dentro de la función
def main(user_id: str):
    return user_id


# Un modelo de Pydantic
class User(BaseModel):
    id: int
    name: str
    joined: date
    