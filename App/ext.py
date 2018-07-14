# -*- coding:utf-8 -*-
#  集成第三方
from flask_cache import Cache
from flask_mail import Mail

from App.apis import init_api
from App.models import init_db

mail = Mail()

cache = Cache(config={'CACHE_TYPE': 'redis',
                           'CACHE_REDIS_HOST': '',
                           'CACHE_REDIS_POST': 6379,
                           'CACHE_REDIS_PASSWORD': '',
                           'CACHE_REDIS_DB': '9',
                           'CACHE_KEY_PREFIX': 'tpp_cache'})
def init_ext(app):
    #  初始化数据库
    init_db(app)

    #  初始化api接口
    init_api(app)
    #  初始化邮箱模块
    mail.init_app(app)
    # 初始化cache模块
    cache.init_app(app)
