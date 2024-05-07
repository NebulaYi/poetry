import re
from datetime import date

from flask import jsonify



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
