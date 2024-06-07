import json
import re
from datetime import date
from sqlite3 import IntegrityError

from app import db
from app.models import Users,Records
import jwt



def is_valid_email(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return 1
    else:
        # 无效
        return 0

def is_valid_pwd(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z]|(?=.*[!@#$%^&*]))[a-zA-Z\d!@#$%^&*]{8,16}$'

    if re.match(pattern, password):
        return 1
    else:
        return 0


def formatData(code,msg,objectlist=[]):
    """
    格式化返回值
    :param code: 校验码
    :param msg: 错误消息
    :param list:查询的列表
    :return:
    """
    dict={}
    dict["code"]=code
    dict["msg"]=msg
    list=[]
    for i in range(len(objectlist)):
        list.append(objectlist[i].to_json())
    dict["data"]=list
    return json.dumps(dict, ensure_ascii=False)


def formatData_ls(code,msg,list=[]):
    dict = {}
    dict["code"] = code
    dict["msg"] = msg
    dict["data"] = list
    return json.dumps(dict, ensure_ascii=False)

def formatData_str(code,msg,list):
    dict = {}
    dict["code"] = code
    dict["msg"] = msg
    dict["data"] = list
    return json.dumps(dict, ensure_ascii=False)

def is_login(request):
    token = request.headers.get("token")
    if not token:
        return 1
    data = jwt.decode(token, 'my_secret_key', algorithms=['HS256'])
    if data['status'] != "login":
        return 1

    return 0


def saveHistoryRecord(email,functionName,question,answer,style):
    record=Records(email=email,style=style,functionName=functionName,description=question,result=answer)
    try:
        db.session.add(record)
        db.session.commit()
        return True
    except Exception as e:
        return False



