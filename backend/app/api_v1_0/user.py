import json
from datetime import datetime, timedelta

import jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from . import api
from flask import request, jsonify, url_for, redirect, flash, render_template, session
from app.models import Users, Records
from .. import db
from ..utils import is_valid_email, is_valid_pwd, formatData as fd, is_login
from werkzeug.security import generate_password_hash, check_password_hash


@api.route("/user/register", methods=['POST'])
def register():
    """
        账号注册
        :return: 返回成功/失败信息
        """
    req_dict = request.get_json()
    name = req_dict["username"]
    email = req_dict["email"]
    password = req_dict["password"]

    if name=="":
        return fd(code=2, msg="用户名为空")
    # 判断email格式
    if is_valid_email(email) == 0:
        return fd(code=2, msg="邮箱格式有误，请重新输入")
    if is_valid_pwd(password) == 0:
        return fd(code=2, msg="密码格式有误，请重新输入")
    # 重复
    user = Users(username=name, email=email, password=generate_password_hash(password))
    try:
        db.session.add(user)
        db.session.commit()

        users = Users.query.filter_by(email=email).all()
        if len(users) != 0:
            # 发送token
            payload = {
                'exp': datetime.now() + timedelta(minutes=30),
                'status': "login"
            }
            key = 'my_secret_key'
            access_token = jwt.encode(payload, key, algorithm='HS256')

            userdic = users[0].to_json()
            dictoken = {"access_token": access_token}

            # 连接用户信息和token
            dic = {**userdic, **dictoken}

            dict = {}
            dict["code"] = 1
            dict["msg"] = "注册成功"
            dict["data"] = dic

            return json.dumps(dict, ensure_ascii=False)

    except IntegrityError as e:
        return fd(code=3, msg="邮箱已注册")
    except Exception as e:
        return fd(code=6, msg="其他问题")


@api.route("/user/login", methods=['POST'])
def login():
    """
    账号登录
    :return: 返回登录成功/失败信息
    """

    req_dict = request.get_json()

    email = req_dict["email"]
    password = req_dict["password"]

    # 判断email格式是否合法
    if is_valid_email(email) == 0:  # 邮箱不合法
        return fd(code=2, msg="邮箱格式有误，请重新输入")
    else:  # 邮箱合法
        user = Users(email=email, password=generate_password_hash(password))
    try:
        users = Users.query.filter_by(email=email).all()
        if len(users) != 0 and check_password_hash(pwhash=users[0].password, password=password):

            # 发送token
            payload = {
                'exp': datetime.now() + timedelta(minutes=30),
                'status': "login"
            }
            key = 'my_secret_key'
            access_token = jwt.encode(payload, key, algorithm='HS256')

            userdic = users[0].to_json()
            dictoken = {"access_token": access_token}

            # 连接用户信息和token
            dic = {**userdic, **dictoken}

            dict = {}
            dict["code"] = 1
            dict["msg"] = "登录成功"
            dict["data"] = dic

            return json.dumps(dict, ensure_ascii=False)

        else:
            return fd(code=5, msg="未查询到用户信息，请检查账号或密码是否有误")
    except Exception as e:
        # 其他异常
        return fd(code=6, msg="其他问题")


@api.route("/logout/check")
def logoutCheck():
    """
    用户登出
    :return: 返回登录成功/失败信息
    """

    if is_login(request) == 1:
        return fd(code=1, msg="登出成功")
    else:
        return fd(code=2, msg="登出失败")


@api.route("/user/history", methods=["GET"])
def getHistory():
    """
    TODO:获取历史列表
    :return:
    """
    """if is_login(request) == 1:
        return fd(code=6, msg="用户未登录")
    if is_login(request) == 1:
        return fd(code=6, msg="用户未登录")"""
    req_dict = request.get_json()
    email = req_dict["email"]
    try:
        records = Records.query.filter(Records.email==email).all()
        return fd(code=1, msg="成功", objectlist=records);
    except Exception as e:
        return fd(code=6, msg="其他问题")


@api.route("/user/modifyUsername", methods=["PUT"])
def modifyUsername():
    req_dict = request.get_json()
    email = req_dict["email"]
    name = req_dict["username"]
    if name=="":
        return jsonify(code=2,msg="用户名不能为空")
    try:
        Users.query.filter(Users.email == email).update({'username': name})
        db.session.commit()
        return jsonify(code=1,msg='修改成功')
    except Exception as e:
        return jsonify(code=6,msg='网页异常')


@api.route("/user/modifyPassword", methods=["PUT"])
def modifyPassword():
    req_dict = request.get_json()
    email = req_dict["email"]
    opwd = req_dict["originPsw"]
    npwd = req_dict["currentPsw"]

    id_list = Users.query.filter_by(email=email).all()
    if not check_password_hash(pwhash=id_list[0].password , password=opwd):  # 密码错误
        return jsonify(msg='密码错误，不能修改',code=3,data=[])
    elif is_valid_pwd(npwd)==0:
        return jsonify(msg='密码格式错误',code=2,data=[])

    try:
        Users.query.filter(Users.email == email).update({'password': generate_password_hash(npwd)})
        db.session.commit()
        return jsonify(msg='修改成功',code=1,data=[])
    except Exception as e:
        return jsonify(msg='异常',code=6,data=[])
