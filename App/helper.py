# -*- coding:utf-8 -*-
import hashlib
from uuid import uuid4

from flask import request, render_template
from flask_mail import Message

import App.ext


# md5加密类
def md5_crypt(txt):
    m = hashlib.md5()
    m.update(txt.encode())
    return m.hexdigest()


#  token生成类
def getToken():
    return md5_crypt(str(uuid4()))



