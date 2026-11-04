from flask import Blueprint

bp_medicos = Blueprint("bp_medicos", __name__)


@bp_medicos.route("/")
def inicio_medicos():

    return "Modulo de medicos funcionando"