from pydantic import BaseModel


class Ingredient(BaseModel):
    name: str
    serving_size: int
    serving_unit: str
    # should serving size be tup/dict?
    protein: int
    fat: int
    carbs: int
