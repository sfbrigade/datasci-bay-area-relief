from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from bayarea_relief.settings import DATABASE_URL, SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
db.init_app(app)

from bayarea_relief.search import search_bp

app.register_blueprint(search_bp)
