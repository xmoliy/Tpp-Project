# -*- coding:utf-8 -*-
# 声明数据库中表对应的模型类
from datetime import datetime

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    db.init_app(app)
    Migrate(app, db)


class BaseId():
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Letter(db.Model, BaseId):
    __tablename__ = 't_letter'
    name = db.Column(db.String(10))


class City(db.Model, BaseId):
    __tablename__ = 't_city'
    parentId = db.Column(db.Integer, default=0)
    regionName = db.Column(db.String(20))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(20))

    letter_id = db.Column(db.Integer, db.ForeignKey(Letter.id))
    letter = relationship('Letter', backref=backref('citys', lazy=True))

class Role(db.Model,BaseId):
    __tablename__ = 't_role'
    #  用户角色
    name = db.Column(db.String(20))
    rights = db.Column(db.Integer,default=1)

class Qx(db.Model,BaseId):
    __tablename__ = 't_qx'
    name  = db.Column(db.String(30))
    rights = db.Column(db.Integer)

class User(db.Model, BaseId):
    __tablename__ = 't_user'
    name = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(50))
    nickname = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(12), unique=True)
    is_active = db.Column(db.Boolean, default=False)
    is_life = db.Column(db.Boolean, default=True)
    regist_time = db.Column(db.DateTime, default=datetime.now)
    last_login_time = db.Column(db.DateTime, onupdate=datetime.now)
    photo1 = db.Column(db.String(200), nullable=True)
    photo2 = db.Column(db.String(200), nullable=True)
    #  权限
    rights = db.Column(db.Integer,default=1)
    role_id = db.Column(db.Integer,db.ForeignKey(Role.id))
    role = relationship('Role',backref=backref('users',lazy=True))



class Movies(db.Model, BaseId):
    __tablename__ = 't_movies'
    showname = db.Column(db.String(50))
    shownameen = db.Column(db.String(50))
    director = db.Column(db.String(20))
    leadingRole = db.Column(db.String(200))
    type = db.Column(db.String(50))
    country = db.Column(db.String(20))
    language = db.Column(db.String(20))
    duration = db.Column(db.Integer)
    screeningmodel = db.Column(db.String(20))
    openday = db.Column(db.DateTime)
    backgroundpicture = db.Column(db.String(200))
    flag = db.Column(db.Integer, default=0)
    isdelete = db.Column(db.Boolean, default=0)


class Cinemas(db.Model, BaseId):
    __tablename__ = 't_cinemas'
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    score = db.Column(db.Float)
    hallnum = db.Column(db.Integer)
    servicecharge = db.Column(db.Float)
    astrict = db.Column(db.Integer)
    flag = db.Column(db.Integer)
    isdelete = db.Column(db.Boolean, default=0)

