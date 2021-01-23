from flask import render_template
from flask_restful import Resource
from flask_weasyprint import render_pdf, HTML
from datetime import datetime
import base64
from io import BytesIO

from repositories import InspectionRepository
import qrcode


class InspectionPdfResource(Resource):
    @staticmethod
    def get(type: str, id: str):
        inspection = InspectionRepository.find_by_id(id)
        img = qrcode.make('https://inspections-frontend.herokuapp.com/#/inspections/' + id + '/confirmations/new')
        template = 'inspection.html' if type == 'adm' else 'inspection-dg.html'

        buf = BytesIO()
        img.save(buf, 'png')
        buf.seek(0)

        html = render_template(
            template,
            inspection=inspection,
            current_date=datetime.now(),
            days=["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"],
            qr_code=base64.b64encode(buf.read()).decode("utf-8")
        )
        buf.close()
        return render_pdf(HTML(string=html))
