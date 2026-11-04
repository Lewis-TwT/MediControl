from flask import Blueprint

bp_pacientes = Blueprint("bp_pacientes", __name__)


@bp_pacientes.route("/")
def inicio_pacientes():

    return "Modulo de pacientes funcionando"