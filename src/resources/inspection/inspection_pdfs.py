from flask import render_template
from flask_restful import Resource
from flask_weasyprint import render_pdf, HTML
from datetime import datetime

from repositories import InspectionRepository
import qrcode


class InspectionPdfResource(Resource):
    @staticmethod
    def get(pdf_type: str, inspection_id: str):
        inspection = InspectionRepository.find_by_id(inspection_id)
        img = qrcode.make('https://inspections-frontend.herokuapp.com/#/inspections/' + inspection_id + '/confirmations/new')
        img.save('src/static/img/inspection_qrcode.png')
        template = 'inspection.html' if pdf_type == 'adm' else 'inspection-dg.html'
        html = render_template(
            template,
            inspection=inspection,
            current_date=datetime.now(),
            days=["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
        )
        return render_pdf(HTML(string=html))
