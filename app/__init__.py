from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cas import CAS

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CAS(app)

from app import views, models