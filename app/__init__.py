from flask import Flask

from app.extensions import db, migrate

from app.medicos.routes import bp_medicos
from app.pacientes.routes import bp_pacientes
from app.citas.routes import bp_citas


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)

    migrate.init_app(app, db)

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

    return app