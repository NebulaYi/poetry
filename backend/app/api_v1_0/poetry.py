from flask import request

from app.api_v1_0 import api
from ..utils import *

style_length_acrosticGenerate={'七言律诗':67,'五言律诗':51,'七言绝句':34,'五言绝句':26}

@api.route("/poetry/acrosticGenerate", methods=['POST'])
def acrosticGenerate():
    req_dict = request.get_json()
    email = req_dict["email"]
    question = req_dict["keyword"] #前缀
    style = req_dict["style"] #风格;
    """
    - 七言律诗 67
    - 五言律诗 51
    - 七言绝句 34
    - 五言绝句 26
    """
    """if is_login(request) == 1:
        return formatData(code=6, msg="用户未登录")"""
    result=generate_samples(prefix=style+"[SEP]"+question,length=style_length_acrosticGenerate[style]);
    if saveHistoryRecord(email=email, style=style, functionName="藏头诗", question=question, answer=result):
        return formatData_str(code=1, msg="成功生成", list=result)
    else:
        return formatData(code=4, msg="保存失败")

style_length_customizeGenerate={'七言律诗':67,'五言律诗':51,'七言绝句':34,'五言绝句':26}
addCount={'七言律诗':8,'五言律诗':8,'七言绝句':4,'五言绝句':4}
@api.route("/poetry/customizeGenerate", methods=['POST'])
def customizeGenerate():
    req_dict = request.get_json()
    email = req_dict["email"]
    question = req_dict["keyword"]
    style = req_dict["style"]
    """
        TODO:获取
        :return:
        """
    """if is_login(request) == 1:
        return formatData(code=6, msg="用户未登录")"""
    result=generate_samples(prefix=style+"[SEP]"+question,length=style_length_customizeGenerate[style]+addCount[style]-len(question));
    if saveHistoryRecord(email=email,style=style,functionName="自定义风格", question=question, answer=result):
        return formatData_str(code=1,msg="成功生成",list=result)
    else:
        return formatData(code=4, msg="保存失败")

