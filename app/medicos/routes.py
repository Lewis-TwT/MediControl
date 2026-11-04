
from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db
from app.models import Medico

bp_medicos = Blueprint("bp_medicos", __name__)


# LISTAR MEDICOS
@bp_medicos.route("/")
def listar():
    medicos = Medico.query.all()
    return render_template("medicos/listar.html", medicos=medicos)


# REGISTRAR MEDICO
@bp_medicos.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        nombre = request.form["nombre"]
        especialidad = request.form["especialidad"]

        medico = Medico(
            nombre=nombre,
            especialidad=especialidad
        )

        db.session.add(medico)
        db.session.commit()

        return redirect(url_for("bp_medicos.listar"))

    return render_template("medicos/formulario.html")


# EDITAR MEDICO
@bp_medicos.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    medico = db.session.get(Medico, id)

    if medico is None:
        return "Medico no encontrado", 404

    if request.method == "POST":
        medico.nombre = request.form["nombre"]
        medico.especialidad = request.form["especialidad"]

        db.session.commit()

        return redirect(url_for("bp_medicos.listar"))

    return render_template("medicos/formulario.html", medico=medico)


# ELIMINAR MEDICO
@bp_medicos.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    medico = db.session.get(Medico, id)

    if medico is None:
        return "Medico no encontrado", 404

    if medico.citas:
        return "No se puede eliminar: el medico tiene citas registradas", 400

    db.session.delete(medico)
    db.session.commit()

    return redirect(url_for("bp_medicos.listar"))
