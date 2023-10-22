from flask import Flask
from flask_smorest import Api

# import blueprints to be registered
from resources.stores import bp as storesBluePrint
from resources.items import bp as itemsBluePrint

app = Flask(__name__)

# configure flask app
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(storesBluePrint)
api.register_blueprint(itemsBluePrint)


if __name__ == "__main__":
    app.run(port=8000, debug=True)

