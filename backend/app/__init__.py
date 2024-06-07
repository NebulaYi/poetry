from flask import Flask,session

from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager

from flask_migrate import Migrate as migrate

db = SQLAlchemy()
def create_app():
    """
    创建flask应用对象
    :param config_name:
    :return:
    """
    app=Flask(__name__,template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@10.135.2.25/movieweb"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['JWT_SECRET_KEY'] = 'my_secret_key'
    app.secret_key='123456'
    #初始化db
    db.init_app(app)

    # 实例化迁移对象
    grate = migrate(app, db)
    jwt = JWTManager(app)

    #注册蓝图
    from . import api_v1_0
    app.register_blueprint(api_v1_0.api,url_prefix="/api/v1.0")

    return app

