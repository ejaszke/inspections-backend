from flask import render_template
from flask_restful import Resource
from flask_weasyprint import render_pdf, HTML
from datetime import datetime

from repositories import InspectionRepository
import qrcode



class InspectionPdfResource(Resource):
    @staticmethod
    def get(id: str):
        inspection = InspectionRepository.find_by_id(id)
        img = qrcode.make('test text')
        img.save('src/static/img/inspection_qrcode.png')
        html = render_template(
            'inspection.html',
            inspection=inspection,
            current_date=datetime.now(),
            days=["niedziela", "poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota"]
        )
        return render_pdf(HTML(string=html))
