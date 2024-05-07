from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app import db

class Users(db.Model):
    __tablename__="users"
    email = db.Column(db.String(40),unique=True,primary_key=True)
    password = db.Column(db.String(17))
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

class records(db.Model):
    __tablename__="records"
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    email = db.Column(db.String(40))
    model_type=db.Column(db.String(40))
    description=db.Column(db.String(255))
    result=db.Column(db.String(255))
    length=db.Column(db.Integer)
    create_time = db.Column(db.DateTime,nullable=False)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

