from flask import render_template
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask_weasyprint import render_pdf, HTML
from datetime import date
# from babel.dates import format_date, format_datetime, format_time

class InspectionPdfResource(Resource):
    @staticmethod
    def get(id: str):
        d = date(2002, 12, 31)
        html = render_template('sample.html', name=id, issue=d)
        return render_pdf(HTML(string=html))
