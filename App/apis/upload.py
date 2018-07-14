# -*- coding:utf-8 -*-
import os
from uuid import uuid4

from flask import request, session
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage

import App.ext
from App import settings, dao
from App.models import User


class UploadApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('img',type=FileStorage,location='files',required=True,help='必须提供一个名为img的file表单参数')
    parser.add_argument('token',required=True,help='必须提供token')


    def post(self):
        args = self.parser.parse_args()
        uFile:FileStorage =args['img']
        newFileName = str(uuid4()).replace('-','')
        newFileName += '.'+uFile.filename.split('.')[-1]

        id = session.get(args['token'])
        user=dao.getById(User,id)
        uFile.save(os.path.join(settings.MEDIA_DIR,newFileName))
        uFile.close()
        user.photo1 = '/static/uploads/' + newFileName
        dao.save(user)

        return {'msg': '上传成功!',
                'path': '/static/uploads/{}'.format(newFileName)}

    # return {'msg': '您可能还没有登录'}
