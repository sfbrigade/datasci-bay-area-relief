from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from bayarea_relief.search import search_bp

app = Flask(__name__)
app.register_blueprint(search_bp)
url = "postgresql://postgres:postgres@localhost:5000/bar"
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning
db = SQLAlchemy(app)
db.init_app(app)

