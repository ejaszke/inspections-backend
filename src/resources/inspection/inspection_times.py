from flask_restful import Resource
from repositories import InspectionRepository, InspectionTimeRepository
from flask_restful.reqparse import Argument
from util import parse_params
from models import InspectionTime
from datetime import date as _date, time


class InspectionTimesResource(Resource):
    @staticmethod
    @parse_params(
        Argument("date", location="json", required=True, help="Missing parameter"),
        Argument("start_time", location="json", required=True, help="Missing parameter"),
        Argument("end_time", location="json", required=True, help="Missing parameter"),
    )
    def post(id: str, date: str, start_time: str, end_time: str):
        inspection = InspectionRepository.find_by_id(id)
        if not inspection:
            return {"message": "Not found"}, 404
        inspection.times.append(InspectionTime(
            date=_date.fromisoformat(date),
            start_time=time.fromisoformat(f"{start_time}:00"),
            end_time=time.fromisoformat(f"{end_time}:00")
        ))
        inspection.save()
        return inspection.json

    @staticmethod
    def delete(inspection_id: str, inspection_time_id: str):
        inspection = InspectionRepository.find_by_id(inspection_id)
        inspection_time = InspectionTimeRepository.find_by_id(inspection_time_id)
        if not inspection or not inspection_time:
            return {"message": "Not found"}, 404
        else:
            inspection.times.remove(inspection_time)
            inspection_time.delete()
            inspection.save()
            return inspection.json
