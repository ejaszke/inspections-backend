from . import db
from .abc import BaseModel, MetaBaseModel
from uuid import uuid4
from datetime import datetime


class InspectionConfirmation(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "inspection_confirmations"

    id = db.Column(db.String(36), primary_key=True)
    inspection_id = db.Column(db.String(36), db.ForeignKey('inspections.id', ondelete="CASCADE"), nullable=False)
    answer = db.Column(db.String(300))
    additional_notes = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, answer, additional_notes):
        self.id = uuid4().__str__()
        self.answer = answer
        self.additional_notes = additional_notes
