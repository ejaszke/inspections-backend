from models import InspectionTime
from datetime import date as _date, time


class InspectionTimeRepository:
    @staticmethod
    def find_by_id(id: str):
        return InspectionTime.query.filter_by(id=id).one()

    @staticmethod
    def update(inspection_time: InspectionTime, date: _date, start_time: time,
               end_time: time, is_repeated, apartment_notes):
        inspection_time.date = date
        inspection_time.start_time = start_time
        inspection_time.end_time = end_time
        inspection_time.is_repeated = is_repeated
        inspection_time.apartment_notes = apartment_notes
        return inspection_time.save()
