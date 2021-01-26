from flask_restful import Resource
from repositories import InspectionRepository, InspectionTimeRepository
from flask_restful.reqparse import Argument
from util import parse_params
from models import InspectionTime
from datetime import date as _date, time
from flask_jwt_extended import jwt_required
from distutils.util import strtobool


class InspectionTimesResource(Resource):
    @staticmethod
    @parse_params(
        Argument("date", location="json", required=True, help="Missing parameter"),
        Argument("start_time", location="json", required=True, help="Missing parameter"),
        Argument("end_time", location="json", required=True, help="Missing parameter"),
        Argument("is_repeated", location="json", required=False, default=False),
        Argument("apartment_notes", location="json", required=False)
    )
    @jwt_required
    def post(inspection_id: str, date: str, start_time: str, end_time: str, is_repeated: bool, apartment_notes: str):
        inspection = InspectionRepository.find_by_id(inspection_id)
        if not inspection:
            return {"message": "Not found"}, 404
        inspection.times.append(
            InspectionTime(
                date=_date.fromisoformat(date),
                start_time=time.fromisoformat(f"{start_time}:00"),
                end_time=time.fromisoformat(f"{end_time}:00"),
                apartment_notes=apartment_notes,
                is_repeated=bool(strtobool(is_repeated))
            ))
        inspection.save()
        return inspection.json

    @staticmethod
    @jwt_required
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

    @staticmethod
    @parse_params(
        Argument("date", location="json", required=True, help="Missing parameter"),
        Argument("start_time", location="json", required=True, help="Missing parameter"),
        Argument("end_time", location="json", required=True, help="Missing parameter"),
        Argument("is_repeated", location="json", required=False),
        Argument("apartment_notes", location="json", required=False)
    )
    @jwt_required
    def put(inspection_id: str, inspection_time_id: str, date: str, start_time: str,
            end_time: str, is_repeated: bool, apartment_notes: str):
        inspection = InspectionRepository.find_by_id(inspection_id)
        inspection_time = InspectionTimeRepository.find_by_id(inspection_time_id)
        if not inspection or not inspection_time:
            return {"message": "Not found"}, 404
        else:
            inspection_time = InspectionTimeRepository.update(
                inspection_time=inspection_time,
                date=_date.fromisoformat(date),
                start_time=time.fromisoformat(f"{start_time}:00"),
                end_time=time.fromisoformat(f"{end_time}:00"),
                apartment_notes=apartment_notes,
                is_repeated=bool(strtobool(is_repeated))
            )
            return inspection_time.json
