
from flask import Flask, redirect, url_for

from app.extensions import db, migrate

from app.medicos.routes import bp_medicos
from app.pacientes.routes import bp_pacientes
from app.citas.routes import bp_citas


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)

    from app import models

    migrate.init_app(app, db)

    # Registrar Blueprints
    app.register_blueprint(
        bp_medicos,
        url_prefix="/medicos"
    )

    app.register_blueprint(
        bp_pacientes,
        url_prefix="/pacientes"
    )

    app.register_blueprint(
        bp_citas,
        url_prefix="/citas"
    )

    # Ruta principal
    @app.route("/")
    def inicio():
        return redirect(url_for("bp_medicos.listar"))

    return app
