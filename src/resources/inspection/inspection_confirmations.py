from flask_restful import Resource
from flask_restful.reqparse import Argument
from util import parse_params
from repositories import InspectionRepository
from models import InspectionConfirmation


class InspectionConfirmationsResource(Resource):
    @staticmethod
    @parse_params(
        Argument("answer", location="json", required=True, help="Missing parameter"),
        Argument("additional_notes", location="json", required=True, help="Missing parameter")
    )
    def post(id: str, answer: str, additional_notes: str):
        inspection = InspectionRepository.find_by_id(id)
        if not inspection:
            return {"message": "Not found"}, 404
        inspection.confirmations.append(
            InspectionConfirmation(
                answer=answer,
                additional_notes=additional_notes
            )
        )
        inspection.save()
        return inspection.json
