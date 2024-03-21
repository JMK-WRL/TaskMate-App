from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from .database import init_db

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

db = SQLAlchemy(app)

from app import routes
