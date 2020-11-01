from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class InspectionConfirmation(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "inspection_confirmations"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)
    inspection_id = db.Column(UUID(as_uuid=True), db.ForeignKey('inspections.id', ondelete="CASCADE"), nullable=False)
    answer = db.Column(db.String(300))
    additional_notes = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, answer, additional_notes):
        self.answer = answer
        self.additional_notes = additional_notes
