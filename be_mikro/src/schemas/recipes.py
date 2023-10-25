from typing import List
from pydantic import BaseModel
from .ingredients import Ingredient


class Recipe(BaseModel):
    name: str
    ingredients: List[Ingredient]
