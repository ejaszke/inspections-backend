from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class InspectionTime(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "inspection_times"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)
    inspection_id = db.Column(UUID(as_uuid=True), db.ForeignKey('inspections.id', ondelete="CASCADE"), nullable=False)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    apartment_notes = db.Column(db.String(300))
    is_repeated = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, date, start_time, end_time, apartment_notes, is_repeated):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.apartment_notes = apartment_notes
        self.is_repeated = is_repeated
