from flask import Blueprint

bp_citas = Blueprint("bp_citas", __name__)


@bp_citas.route("/")
def inicio_citas():

    return "Modulo de citas funcionando"