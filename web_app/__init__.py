from flask import Flask
from flask_cors import CORS
from web_app.routes.home_routes import home_routes
from web_app.routes.predict_routes import predict_routes

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.register_blueprint(home_routes)
    app.register_blueprint(predict_routes)
    # app.config['CORS_HEADERS'] = 'Content-Type'

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)