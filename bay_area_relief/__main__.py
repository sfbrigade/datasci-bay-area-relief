from flask import Flask
from bay_area_relief.search import search_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(search_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
