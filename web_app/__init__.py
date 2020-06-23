from flask import Flask
from flask_cors import CORS

from web_app.routes.home_routes import home_routes

DATABASE_URL = "sqlite:///test_environment.db"

def create_app():
    app = Flask(__name__)

    cors = CORS(app)

    app.register_blueprint(home_routes)
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)