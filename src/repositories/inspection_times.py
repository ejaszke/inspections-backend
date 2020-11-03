from models import InspectionTime
from datetime import date as _date, time


class InspectionTimeRepository:
    @staticmethod
    def find_by_id(id: str):
        return InspectionTime.query.filter_by(id=id).one()

    @staticmethod
    def update(inspection_time: InspectionTime, date: _date, start_time: time, end_time: time):
        inspection_time.date = date
        inspection_time.start_time = start_time
        inspection_time.end_time = end_time
        return inspection_time.save()
