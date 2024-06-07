
from flask import Blueprint
#创建蓝图对象
api=Blueprint("api_v1_0",__name__)
from . import user,poetry
