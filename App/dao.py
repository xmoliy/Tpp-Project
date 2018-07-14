# -*- coding:utf-8 -*-
#  自定义数据库的功能函数
from flask_sqlalchemy import BaseQuery

from App.models import db


def query(cls) -> BaseQuery:
    return db.session.query(cls)


def queryAll(cls):
    return query(cls).all()


def getById(cls,id):
    try:
        return db.session.query(cls).get(int(id))
    except:
        pass


def save(obj) -> bool:
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        print(e)
        return False
    return True


def delete(obj) -> bool:
    try:
        db.session.delete(obj)
        db.session.commit()
    except:
        return False
    return True


def login(cls,username,password):
    return query(cls).filter(db.and_(cls.name==username,cls.password==password,cls.is_active ==True,cls.is_life==True)).first()
