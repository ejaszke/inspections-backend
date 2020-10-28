from . import db
from .abc import BaseModel, MetaBaseModel
from uuid import uuid4
from datetime import datetime


class Inspection(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "inspections"

    # to_json_filter = ('times', 'confirmations')

    id = db.Column(db.String(36), primary_key=True)
    city = db.Column(db.String(100), nullable=True)
    street = db.Column(db.String(300))
    street_number = db.Column(db.String(10))
    staircases = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    times = db.relationship('InspectionTime')
    confirmations = db.relationship('InspectionConfirmation')

    def __init__(self, city, street, street_number, staircases):
        self.id = uuid4().__str__()
        self.city = city
        self.street = street
        self.street_number = street_number
        self.staircases = staircases
