# pylint: disable=C0411
import logging

from flask import Flask
from flask_migrate import Migrate

from app.main.config.app_config import app_config
from app.main.config.cors_config import configure_cors
from app.main.config.error_handlers_config import configure_error_handlers
from app.main.config.jinja_config import configure_jinja
from app.main.config.limiter_config import configure_limiter
from app.main.config.logging_config import configure_logging
from app.main.config.routes_config import configure_routes

from app.models import db

logger = logging.getLogger(__name__)
migrate = Migrate()


def create_app(is_rate_limit_enabled=True) -> Flask:
    configure_logging(app_config.logging_level)

    logger.info("Starting app...")

    app = Flask(__name__, static_folder="static", static_url_path="/assets")

    app.secret_key = app_config.flask.app_secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.postgres.sql_alchemy_database_url

    db.init_app(app)
    migrate.init_app(app, db)

    configure_routes(app)
    configure_error_handlers(app)
    configure_limiter(app, is_rate_limit_enabled)
    configure_jinja(app)
    configure_cors(app)

    logger.info("Running app...")

    return app
