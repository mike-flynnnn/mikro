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


class Ingredient(BaseModel):
    name: str
    serving_size: int
    serving_unit: str
    # should serving size be tup/dict?
    protein: int
    fat: int
    carbs: int


class Recipe(BaseModel):
    name: str
    ingredients: List[Ingredient]


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    gender: Gender
    roles: List[Role]
    recipes: Optional[List[Recipe]]


class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
