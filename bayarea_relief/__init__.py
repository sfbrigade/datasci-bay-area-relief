from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
url = "postgresql://postgres:postgres@localhost:5000/bar"
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning
db = SQLAlchemy(app)
db.init_app(app)

from bayarea_relief.search import search_bp

app.register_blueprint(search_bp)
