# -*- coding:utf-8 -*-
from flask import request, session
from flask_restful import Resource, reqparse, fields, marshal, marshal_with
from flask_sqlalchemy import BaseQuery

from App import dao, settings
from App.models import Movies, User, Qx
from App.settings import QX


def check_login(qx):
    def check(fn):
        def wrapper(*args, **kwargs):
            token = request.args['token']
            user_id = session[token]
            if not user_id:
                return {'msg': '用户必须先登录'}
            loginUser = dao.getById(User, user_id)
            if loginUser.rights & qx == qx:
                return fn(*args, **kwargs)
            else:
                qxObj = dao.query(Qx).filter(Qx.rights == qx).first()
                return {'msg': '用户没有{}权限'.format(qxObj.name)}

        return wrapper

    return check


class MovieApi(Resource):
    #  定制输入参数
    parser = reqparse.RequestParser()
    parser.add_argument('flag', type=int, help='必须指定影片的类型')
    parser.add_argument('city', default='')
    parser.add_argument('region', default='')
    parser.add_argument('orderby', default='openday')
    parser.add_argument('sort', default=1)
    parser.add_argument('page', default=1, type=int, help='页码必须是数值')
    parser.add_argument('limit', default=10, type=int, help='每页显示的大小必须是数值')

    out_fields = {
        'returnCode': fields.String(default='0'),
        'returnValue': fields.Nested({
            'country': fields.String,
            'director': fields.String,
            'duration': fields.String,
            'showname': fields.String,
            'shownameen': fields.String,
            'leadingRole': fields.String,
            'type': fields.String,
            'language': fields.String,
            'screeningmodel': fields.String,
            'openday': fields.String,
            'flag': fields.Integer}),

    }

    # out_fields = {
    #     'msg': fields.String,
    #     'data': fields.Nested(out_movie_fields),
    # }

    # @marshal_with(out_fields)
    def get(self):
        args = self.parser.parse_args()
        flag = args['flag']
        qs: BaseQuery = dao.query(Movies).filter(Movies.flag == flag)

        sort = args['sort']
        qs: BaseQuery = qs.order_by(('-' if sort == 1 else '') + args.get('orderby'))
        page = qs.paginate(args.get('page'), args.get('limit'))
        data = {'returnValue': page.items}
        # return marshal({'returnValue':data},self.out_fields)
        return marshal(data, self.out_fields)
        # return {'returnValue':data}

    @check_login(QX.DELETE_QX)
    def delete(self):
        mid = request.args['id']
        movie = dao.getById(Movies, mid)
        if not movie:
            return {'msg': '你要删除的影片不存在'}
        dao.delete(movie)
        return {'msg': movie.showname+'删除成功'}

        #
        # #  从session中获取登录用户的TOKEN
        # token = request.args['token']
        # if not token:
        #     return {'msg': '没有token'}
        # user_id =session[token]
        # if not user_id:
        #     return {'msg': '没有用户ID'}
        #
        # #删除影片功能
        # loginUser = dao.getById(User,user_id)
        # if loginUser.rights & settings.QX.DELETE_QX == settings.QX.DELETE_QX :
        #     # 当前用户有删除权限
        #
        # return {'msg': '充值开通此功能'}
