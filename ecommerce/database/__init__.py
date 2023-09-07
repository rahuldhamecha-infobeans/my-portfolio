import os
from ecommerce import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Rahul21896@localhost/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


def create_db():
    db = SQLAlchemy(app)
    return db


db = create_db()
Migrate(app, db)

import ecommerce.database.register_models
