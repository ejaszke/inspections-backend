from . import db
from .abc import BaseModel, MetaBaseModel
from uuid import uuid4


class InspectionTime(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "inspection_times"

    id = db.Column(db.String(36), primary_key=True)
    inspection_id = db.Column(db.String(36), db.ForeignKey('inspections.id', ondelete="CASCADE"), nullable=False)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)

    def __init__(self, date, start_time, end_time):
        self.id = uuid4().__str__()
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
