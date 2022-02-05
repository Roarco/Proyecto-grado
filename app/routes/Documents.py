import os
import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.Documents import documentService
import app


Documents = Blueprint("documents", __name__)

@Documents.route("/upload" , methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        codigo_Student = request.form["codigo_Student"]
        datetime_document = datetime.datetime.now()
        id_state = 1
        student_observation = request.form["observacion"]
        administrative_code = None
        administrative_observation = None
        file = request.files["file"]
        file.save(os.path.join(app.files, f"{codigo_Student} .pdf"))
        new_document = documentService.create_document(
            codigo_Student, datetime_document, id_state, student_observation, administrative_code, administrative_observation
        )
        return new_document


    return redirect(url_for("students.home_student"))
