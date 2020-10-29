from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources import InspectionsResource
from resources import InspectionResource


INSPECTION_BLUEPRINT = Blueprint("inspection", __name__)

CORS(INSPECTION_BLUEPRINT)

Api(INSPECTION_BLUEPRINT).add_resource(
    InspectionsResource, "/inspections"
)

Api(INSPECTION_BLUEPRINT).add_resource(
    InspectionResource, "/inspections/<string:id>"
)
