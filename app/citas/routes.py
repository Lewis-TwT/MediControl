
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

from app.extensions import db
from app.models import Cita, Medico, Paciente

bp_citas = Blueprint("bp_citas", __name__)


# LISTAR CITAS
@bp_citas.route("/")
def listar():
    citas = Cita.query.all()
    return render_template("citas/listar.html", citas=citas)


# REGISTRAR CITA
@bp_citas.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == "POST":
        fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d").date()
        hora = datetime.strptime(request.form["hora"], "%H:%M").time()

        cita = Cita(
            fecha=fecha,
            hora=hora,
            medico_id=int(request.form["medico_id"]),
            paciente_id=int(request.form["paciente_id"])
        )

        db.session.add(cita)
        db.session.commit()

        return redirect(url_for("bp_citas.listar"))

    return render_template(
        "citas/formulario.html",
        medicos=medicos,
        pacientes=pacientes
    )


# EDITAR CITA
@bp_citas.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    cita = db.session.get(Cita, id)

    if cita is None:
        return "Cita no encontrada", 404

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == "POST":
        cita.fecha = datetime.strptime(
            request.form["fecha"], "%Y-%m-%d"
        ).date()

        cita.hora = datetime.strptime(
            request.form["hora"], "%H:%M"
        ).time()

        cita.medico_id = int(request.form["medico_id"])
        cita.paciente_id = int(request.form["paciente_id"])

        db.session.commit()

        return redirect(url_for("bp_citas.listar"))

    return render_template(
        "citas/formulario.html",
        cita=cita,
        medicos=medicos,
        pacientes=pacientes
    )


# ELIMINAR CITA
@bp_citas.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    cita = db.session.get(Cita, id)

    if cita is None:
        return "Cita no encontrada", 404

    db.session.delete(cita)
    db.session.commit()

    return redirect(url_for("bp_citas.listar"))
