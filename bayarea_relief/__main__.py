from flask import Flask
from bayarea_relief.search import search_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(search_bp)
    return app


def main():
    app = create_app()
    app.run(host="0.0.0.0", port=8080)

