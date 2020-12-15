from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources.inspection import InspectionsResource
from resources.inspection import InspectionResource
from resources.inspection import InspectionTimesResource
from resources.inspection.inspection_pdfs import InspectionPdfResource
from resources.inspection import InspectionConfirmationsResource

INSPECTION_BLUEPRINT = Blueprint("inspections", __name__)

CORS(INSPECTION_BLUEPRINT, resources={r"/api/*": {"origins": "https://inspections-frontend.herokuapp.com"}})

Api(INSPECTION_BLUEPRINT).add_resource(
    InspectionsResource, "/inspections"
)

Api(INSPECTION_BLUEPRINT).add_resource(
    InspectionPdfResource, "/pdfs/<string:id>"
)

Api(INSPECTION_BLUEPRINT).add_resource(
    InspectionResource, "/inspections/<string:id>"
)

Api(INSPECTION_BLUEPRINT).add_resource(
    InspectionTimesResource,
    "/inspections/<string:id>/times",
    "/inspections/<string:inspection_id>/times/<string:inspection_time_id>",
)

Api(INSPECTION_BLUEPRINT).add_resource(
    InspectionConfirmationsResource,
    "/inspections/<string:id>/confirmations"
)