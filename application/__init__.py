from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from os import urandom
app = Flask(__name__)
SECRET_KEY = urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app)
 
from application.routes import *