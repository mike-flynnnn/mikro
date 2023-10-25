from typing import List
from uuid import uuid4
from ..schemas.users import User, Gender, Role

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Wright",
        gender=Gender.female,
        roles=[Role.user],
        recipes=[]
    ),
    User(
        id=uuid4(),
        first_name="Mike",
        last_name="Flynn",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
        recipes=[]
    )
]
