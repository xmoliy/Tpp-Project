# -*- coding:utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
STATIC_DIR = os.path.join(BASE_DIR, 'App/static')
MEDIA_DIR = os.path.join(STATIC_DIR, 'uploads')


class Config():
    ENV = 'development'
    # DEBUG = 'True'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxx@xx.xx.xx.xx/tpp'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
    SECRET_KEY = '123'

    # 配置邮箱
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'xx@163.com'
    MAIL_PASSWORD = 'xxxx'
    # MAIL_DEBUG = 'app.debug'
    # MAIL_USE_SSL = True
    # MAIL_PORT = 456
    MAIL_DEFAULT_SENDER = 'xxxx@163.com'


class QX():
    QUERY_QX = 1
    EDIT_QX = 2
    DELETE_QX = 4
    ADD_QX = 8
    MAIL_QX = 16
    PALY_QX = 32
