from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Divvys(db.Model):

    __tablename__ = 'divvytable'
    trip_id = db.Column(
        db.Integer,
        primary_key=True
    )
    start_time = db.Column(
        db.DateTime(45),
        nullable=False
    )
    stop_time = db.Column(
        db.DateTime(45),
        nullable=False
    )
    bike_id = db.Column(
        db.Integer,
        nullable=False
    )
    from_station_id = db.Column(
        db.Integer,
        nullable=True
    )
    from_station_name = db.Column(
        db.String(45),
        nullable=False
    )
    to_station_id = db.Column(
        db.Integer,
        nullable=False
    )
    to_station_name = db.Column(
        db.String(45),
        nullable=False
    )
    usertype = db.Column(
        db.String(45),
        nullable=False
    )
    gender = db.Column(
        db.String(45),
        nullable=False
    )
    birthday = db.Column(
        db.String(45),
        nullable=False
    )
    trip_duration = db.Column(
        db.Integer,
        nullable=False
    )