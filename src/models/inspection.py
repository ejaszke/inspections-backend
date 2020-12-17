from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Inspection(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "inspections"

    # to_json_filter = ('times', 'confirmations')

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)
    city = db.Column(db.String(100), nullable=True)
    street = db.Column(db.String(300))
    street_number = db.Column(db.String(10))
    staircases = db.Column(db.String(100))
    employee = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    times = db.relationship('InspectionTime', cascade="all, delete", passive_deletes=True)
    confirmations = db.relationship('InspectionConfirmation', cascade="all, delete", passive_deletes=True)

    def __init__(self, city, street, street_number, staircases, employee):
        self.city = city
        self.street = street
        self.street_number = street_number
        self.staircases = staircases
        self.employee = employee
