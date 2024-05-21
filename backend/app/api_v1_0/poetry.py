from flask import request

from app.api_v1_0 import api
from ..utils import *

@api.route("/poetry/basicGenerate", methods=['POST'])
def basicGenerate():
    req_dict = request.get_json()
    email = req_dict["email"]
    question = req_dict["keyword"]
    modeltype = req_dict["modeltype"]
    """
    TODO:获取对话
    :return:
    """

    saveHistoryRecord(email, "基础诗词生成", question, "ans", modeltype, 5,"")

    return


@api.route("/poetry/acrosticGenerate", methods=['POST'])
def acrosticGenerate():
    req_dict = request.get_json()
    email = req_dict["email"]
    question = req_dict["keyword"]
    length = req_dict["length"]
    style = req_dict["style"]
    """
        TODO:获取
        :return:
        """

    saveHistoryRecord(email,"functionName", question, "answer", "modeltype", length ,style)
    return


@api.route("/poetry/customizeGenerate", methods=['POST'])
def customizeGenerate():
    req_dict = request.get_json()
    email = req_dict["email"]
    question = req_dict["keyword"]
    modeltype = req_dict["modeltype"]
    length = req_dict["length"]
    style = req_dict["style"]
    """
        TODO:获取
        :return:
        """

    saveHistoryRecord(email, "functionName", question, "answer", modeltype, length,style)
    return
