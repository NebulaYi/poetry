from sqlalchemy.exc import IntegrityError

from . import api
from flask import request, jsonify, url_for, redirect, flash, render_template, session
from app.models import Users
from ..utils import is_valid_email

"""@api.route("/login")
def login():

    return render_template("login.html")
"""

@api.route("/login/check",methods=['POST'])
def loginCheck():
    """
    账号登录
    :return:
    """
    req_dict = request.get_json()
    #------改--------#
    account=req_dict["account"]
    password=req_dict["password"]
    user=Users()

    flag=""  #email or phone

    #判断email格式是否合法
    if is_valid_email(account)==0:
        # Email不合法，判断手机是否合法
        if is_valid_phone(account)==0:#手机不合法
            #flash('邮箱或手机号格式有误，请重新输入')
            """return redirect(url_for('api_v1_0.register'))"""
            return jsonify(msg='邮箱或手机号格式有误，请重新输入')
        else:# 手机合法
            user = Users(phone=account, password=password)  #
            flag="phone"
    else:#邮箱合法
        user = Users(email=account, password=password)
        flag="email"
    try:
        if flag=="phone":
            users=Users.query.filter_by(phone=account,password=password)
            if len(users) != 0:

                session["userID"]=users[0].id

                return jsonify(msg='登录成功')
            else:
                return jsonify(msg='账号或密码错误')
        else:
            users=Users.query.filter_by(email=account,password=password).all()
            if len(users) != 0:

                session["userID"] = users[0].id

                return jsonify(msg='登录成功')
            else:
                return jsonify(msg='账号或密码错误')
    except Exception as e:
        # 其他异常
        #flash('其他异常')
        """return redirect(url_for('api_v1_0.register'))"""
        return jsonify(msg='网页异常')


@api.route("/logout/check")
def logoutCheck():
    if session.get("userID") is not None:
        session.pop("userID")
        return jsonify(msg='登出成功')
    else:
        print(session.get("userID"))
        return jsonify(msg='未登录')
