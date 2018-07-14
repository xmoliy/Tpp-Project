# -*- coding:utf-8 -*-
from flask_restful import Api, Resource

from App.apis.account import AccountApi
from App.apis.city import CityApi
from App.apis.movie import MovieApi
from App.apis.upload import UploadApi
from App.apis.user import UserApi
api = Api()  # 创建RESTfull的Api对象


def init_api(app):
    api.init_app(app)


# class CityResource(Resource):
#     pass
#
#
# class UserResource(Resource):
#     pass
#
#
# class AccountResource(Resource):
#     pass
#
#
# class UserLoginResource(Resource):
#     pass
#
#
# class MovieResource(Resource):
#     pass
#
#
# class MyMovieResource(Resource):
#     pass

api.add_resource(CityApi, '/city')
api.add_resource(UserApi, '/user')
api.add_resource(AccountApi, '/account')
api.add_resource(UploadApi, '/upload')
api.add_resource(MovieApi, '/movies')
# api.add_resource(UserLoginApi,'/login')
# api.add_resource(MyMovieResource,'/mymovies')
