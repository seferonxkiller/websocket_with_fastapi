from typing import Dict

from models.users import User


class DummyDatabase:
    users: Dict[int, User] = {}


db = DummyDatabase()