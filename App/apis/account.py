# -*- coding:utf-8 -*-
from datetime import datetime
from uuid import uuid4

from flask import request, session
from flask_restful import Resource, reqparse, fields, marshal

import App.ext
from App import dao, helper
from App.dao import save
from App.helper import md5_crypt, getToken
from App.models import User


class AccountApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('opt', required=True, help='没有声明opt的操作')

    def get(self):
        args = self.parser.parse_args()
        opt = args.get('opt')
        if opt == 'active':
            activeParser = self.parser.copy()
            activeParser.add_argument('token', required=True, help='必须提供激活的token')
            args = activeParser.parse_args()  # 验证请求参数
            token = args.get('token')
            # 进一步处理
            user_id = App.ext.cache.get(token)
            if user_id:
                user = dao.getById(User, user_id)
                user.is_active = True
                save(user)
                App.ext.cache.clear()
                return {'msg': '{}用户激活成功'.format(user.name)}
            else:
                reactive_url = request.host_url + 'account?opt=reactive'
                return {'msg': '验证码已经过期' + reactive_url}
        elif opt == 'login':
            return self.login()
        elif opt == 'reactive':
            return self.reactive()
        elif opt == 'logout':
            return self.logout()
        elif opt == 'modifyPasswd':
            return self.modifyPasswd()

    def reactive(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, help='必须提供邮箱')
        args = parser.parse_args()
        email = args.get('email')
        qs = dao.query(User).filter(User.email.__eq__(email))
        if not qs.count():
            return {'status': 661, 'msg': '该邮箱未注册'}
        helper.sendEmail(qs.first())
        return {'msg': '重写申请用户激活成功，请去邮箱查收'}

    def login(self):
        loginParser = self.parser.copy()
        loginParser.add_argument('username', required=True, help='用户登录必须提供用户名')
        loginParser.add_argument('password', required=True, help='用户登录必须提供口令')
        args = loginParser.parse_args()

        username = args.get('username')
        password = args.get('password')
        user = dao.login(User, username, md5_crypt(password))
        print(user)
        if user:
            token = getToken()
            user.last_login_time = datetime.today()
            dao.save(user)
            session[token] = user.id

            out_user_fields = {
                'name': fields.String,
                'email': fields.String,
                'phone': fields.String,
                'photo1': fields.String(attribute='photo_1')

            }

            out_fields = {
                'msg': fields.String,
                'data': fields.Nested(out_user_fields),
                'access_token': fields.String

            }

            data = {'msg': '登录成功',
                    'data': user,
                    'access_token': token}

            return marshal(data, out_fields)

        return {'msg': '用户登录失败'}

    def logout(self):
        myParser = self.parser.copy()
        myParser.add_argument('token', required=True, help='Token不能为空')
        args = myParser.parse_args()
        token = args['token']
        user_id = session.get(token)
        if not user_id:
            return {'status': 667, 'msg': '您可能还没有登录'}
        session.pop(token)
        return {'status': 200, 'msg': '用户登出成功'}

    def modifyPasswd(self):
        modifyParser = self.parser.copy()
        modifyParser.add_argument('username', required=True, help='用户登录必须提供用户名')
        modifyParser.add_argument('password', required=True, help='用户登录必须提供口令')
        modifyParser.add_argument('newpassword', required=True, help='新密码不能为空')
        args = modifyParser.parse_args()
        username = args['username']
        password = args['password']
        newpassword = args['newpassword']
        user = dao.login(User, username, md5_crypt(password))
        if user:
            user.password = md5_crypt(newpassword)
            save(user)
            return {'msg': '{}用户密码修改成功'.format(user.name)}
        return {'msg': '用户密码修改失败'}
