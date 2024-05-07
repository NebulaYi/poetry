from app.api_v1_0 import api


@api.route("/poetry/basicGenerate", methods=['POST'])
def basicGenerate():
    return


@api.route("/poetry/acrosticGenerate", methods=['POST'])
def acrosticGenerate():
    return


@api.route("/poetry/customizeGenerate", methods=['POST'])
def customizeGenerate():
    return