from . import db
from .abc import BaseModel, MetaBaseModel
from uuid import uuid4


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    to_json_filter = ("password",)

    def __init__(self, email, password):
        """ Create a new User """
        self.id = uuid4().__str__()
        self.email = email
        self.password = password
