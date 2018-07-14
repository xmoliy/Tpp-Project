# -*- coding:utf-8 -*-
from flask_restful import Resource, fields, marshal_with

from App import dao
from App.models import Letter


class CityApi(Resource):
    city_fields = {
        'id': fields.Integer,
        'parentId': fields.Integer,
        'regionName': fields.String,
        'cityCode': fields.Integer,
        'pinYin': fields.String
    }
    values_fields = {
        # 'A': fields.Nested(city_fields)

    }

    out_fields = {
        'returnCode': fields.Integer,
        'returnValue': fields.Nested(values_fields)

    }
    @marshal_with(out_fields)
    def get(self):
        letters = dao.queryAll(Letter)
        returnValue={}
        for letter in letters:
            self.values_fields[letter.name]=fields.Nested(self.city_fields)
            returnValue[letter.name]=letter.citys

        return {'returnValue':returnValue}
