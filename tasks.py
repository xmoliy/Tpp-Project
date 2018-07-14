# -*- coding:utf-8 -*-
from celery import Celery
from flask import request, render_template
from flask_mail import Message
import App
from App import dao
from App.models import User
from App.helper import getToken

try:
    import manage
except:
    pass

celery = Celery('tasks', broker='redis://:8227099@120.79.223.66:6379/5')


# #  发送验证码类
# def sendEmail(u):


@celery.task
def sendMail(uId,active_url):
    with manage.app.test_request_context():
        u = dao.getById(User, uId)

        token = getToken()


        App.ext.cache.set(token, u.id, timeout=60 * 10)
        active_url = active_url + token
        msg = Message(subject='淘票票用户激活', recipients=[u.email])
        msg.html = render_template('msg.html', username=u.name, active_url=active_url)
        try:
            App.ext.mail.send(msg)
            print('邮件已发送')

        except Exception as e:
            print('邮件发送失败')

