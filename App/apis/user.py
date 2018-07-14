# -*- coding:utf-8 -*-
from uuid import uuid4

from flask import request
from flask_mail import Message
from flask_restful import Resource, reqparse

import tasks
from App import dao
import App.ext
from App.helper import md5_crypt
from App.models import User


class UserApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', dest='name', required=True, help='用户名不能为空')

    def post(self):
        # 从基本的请求解析器中复制请求参数
        registParser = self.parser.copy()

        # 再添加注册时使用的
        registParser.add_argument('password', dest='pwd', required=True, help='密码不能为空')
        registParser.add_argument('nickname', required=True, help='昵称不能为空')
        registParser.add_argument('email', required=True, help='邮箱不能为空')
        registParser.add_argument('phone', required=True, help='手机号不能为空')

        args = registParser.parse_args()

        u = User()
        u.name = args['name']
        u.nickname = args['nickname']
        u.email = args['email']
        u.phone = args['phone']
        u.password = md5_crypt(args['pwd'])

        if dao.save(u):
            # token = md5_crypt(str(uuid4()))
            # App.ext.cache.set(token, u.id, timeout=60 * 10)
            active_url = request.host_url + 'account?opt=active&token='
            # msg = Message(subject='淘票票用户激活', recipients=[u.email], sender='disenqf@163.com')
            # msg.html = '<h1>{}注册成功</h1><h3><a href={}>点击这里验证邮件</a></h3><h2>或者复制地址到浏览器: {}'.format(u.name, active_url,
            #                                                                                       active_url)
            #
            # App.ext.mail.send(msg)

            tasks.sendMail.delay(u.id,active_url)
            return {'status': 666, 'msg': '用户注册成功'}
        return {'status': 660, 'msg': '用户注册失败'}

    def get(self):
        #  验证用户名是否已经注册
        args = self.parser.parse_args()
        name = args['name']
        qs = dao.query(User).filter(User.name == name)
        if qs.count():
            return {'status': 202, 'msg': name + '用户名被注册'}
        return {'status': 200, 'msg': name + '用户名可以注册'}
