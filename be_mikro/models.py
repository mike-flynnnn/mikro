from ast import Num
from typing import Optional, List
from uuid import UUID, uuid4
from click import Option
from pydantic import BaseModel
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    user = "user"


class Gender(str, Enum):
    male = "male"
    female = "female"


class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]


class Ingredient(BaseModel):
    name: str
    serving_size: Num
    serving_unit: str
    # should serving size be tup/dic?
    protein: Num
    fat: Num
    carbs: Num


class Recipe(BaseModel):
    name: str
    ingredients: List[Ingredient]

# how to calculate total macros/calories for a recipe?
