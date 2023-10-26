from flask import Flask
from flask_smorest import Api
import os
# import blueprints to be registered
from resources.stores import bp as storesBluePrint
from resources.items import bp as itemsBluePrint

# import database
from db import db
import models


def create_app(db_url=None):
    app = Flask(__name__)

    # configure flask app
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize db and connect to the flask app
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(storesBluePrint)
    api.register_blueprint(itemsBluePrint)

    return app

if __name__ == "__main__":
    pass
    # app.run(port=8000, debug=True)

