from sqlalchemy.exc import IntegrityError

from . import api
from flask import request, jsonify, url_for, redirect, flash, render_template, session
from app.models import Users
from .. import db
from ..utils import is_valid_email, is_valid_pwd


@api.route("/register/user", methods=['POST'])
def register():
    """
    账号登录
    :return:
    """
    req_dict = request.get_json()
    # ------改--------#
    mail = req_dict["email"]
    password = req_dict["password"]
    user = Users()

    if is_valid_email(mail) == 0:
        return jsonify(msg='email invalid', code=400, data=False)
    if is_valid_pwd(password) == 0:
        return jsonify(msg='password invalid', code=400, data=False)

    if is_valid_email(mail) == 1 and is_valid_pwd(password) == 1:
        user = Users(email=mail, password=password)

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(msg='注册成功', code=200, data=True)

    except IntegrityError as e:
        # 邮箱出现重复值，用户邮箱已注册过
        # flash('手机号已注册')
        """return redirect(url_for('api_v1_0.register'))"""
        return jsonify(msg='邮箱已注册', code=400, data=False)
    except Exception as e:
        # 其他异常
        # flash('其他异常')
        """return redirect(url_for('api_v1_0.register'))"""
        return jsonify(msg='网页异常', code=401, data=False);


@api.route("/login/user", methods=['POST'])
def login():
    """
        账号登录
        :return:
        """
    req_dict = request.get_json()
    # ------改--------#
    mail = req_dict["email"]
    password = req_dict["password"]

    try:
        users = Users.query.filter_by(email=mail, password=password).all()
        if len(users) != 0:
            return jsonify(msg="login success", code=200, data=True)
        else:
            if (len(Users.query.filter_by(email=mail).all())) != 0:
                return jsonify(msg="password error", code=400, data=False)
            else:
                return jsonify(msg="user not exists", code=400, data=False)


    except Exception as e:

        # 其他异常

        # flash('其他异常')

        """return redirect(url_for('api_v1_0.register'))"""

        return jsonify(msg='网页异常')
