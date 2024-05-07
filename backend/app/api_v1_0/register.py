from sqlalchemy.exc import IntegrityError
from . import api
from app import db
from flask import request, jsonify, url_for, redirect, flash, render_template
from app.models import Users
from ..utils import is_valid_email

"""@api.route("/register")
def register():

    return render_template("register.html")
"""

@api.route("/register/check",methods=['POST'])
def registerCheck():
    """
    账号注册
    :return:
    """
    req_dict = request.get_json()
    #------改--------#
    name=req_dict["name"]
    email=req_dict["email"]
    password=req_dict["password"]
    #password2=req_dict("password2")
    user=Users()

    #判断email格式
    if is_valid_email(email)==0:
        #flash('邮箱格式有误，请重新输入')
        """return redirect(url_for('api_v1_0.register'))"""
        return jsonify(msg='邮箱格式有误，请重新输入')
    #重复
    user = Users(name=name,email=email,password=password)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(msg='注册成功')
    except IntegrityError as e:
        # 邮箱出现重复值，用户邮箱已注册过
        #flash('手机号已注册')
        """return redirect(url_for('api_v1_0.register'))"""
        return jsonify(msg='邮箱已注册')
    except Exception as e:
        # 其他异常
        #flash('其他异常')
        """return redirect(url_for('api_v1_0.register'))"""
        return jsonify(msg='网页异常')

