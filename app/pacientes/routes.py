
from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db
from app.models import Paciente

bp_pacientes = Blueprint("bp_pacientes", __name__)


# LISTAR PACIENTES
@bp_pacientes.route("/")
def listar():
    pacientes = Paciente.query.all()
    return render_template("pacientes/listar.html", pacientes=pacientes)


# REGISTRAR PACIENTE
@bp_pacientes.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]

        paciente = Paciente(
            nombre=nombre,
            telefono=telefono
        )

        db.session.add(paciente)
        db.session.commit()

        return redirect(url_for("bp_pacientes.listar"))

    return render_template("pacientes/formulario.html")


# EDITAR PACIENTE
@bp_pacientes.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    paciente = db.session.get(Paciente, id)

    if paciente is None:
        return "Paciente no encontrado", 404

    if request.method == "POST":
        paciente.nombre = request.form["nombre"]
        paciente.telefono = request.form["telefono"]

        db.session.commit()

        return redirect(url_for("bp_pacientes.listar"))

    return render_template("pacientes/formulario.html", paciente=paciente)


# ELIMINAR PACIENTE
@bp_pacientes.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    paciente = db.session.get(Paciente, id)

    if paciente is None:
        return "Paciente no encontrado", 404

    if paciente.citas:
        return "No se puede eliminar: el paciente tiene citas registradas", 400

    db.session.delete(paciente)
    db.session.commit()

    return redirect(url_for("bp_pacientes.listar"))
