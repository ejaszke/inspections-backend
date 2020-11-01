from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    to_json_filter = ("password",)

    def __init__(self, email, password):
        self.email = email
        self.password = password
