from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

from src.libs.error_code import AuthFailed
from src.models.user import User
from collections import namedtuple
#

auth = HTTPBasicAuth()

UserNamedTuple = namedtuple('UserNamedTuple', ['uid', 'category', 'scope'])


# 回调函数
@auth.verify_password
def verify_password(token, password):
    # user = User().query.filter_by(email=username).first()
    # if user and check_password_hash(user.password, password):
    #     return True
    print('token', token)
    user_info = verify_auth_token(token)
    print('user_info', user_info)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


# 生成token
def generate_auth_token(uid, category, scope=None):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    json_data = {'uid': uid, 'category': category, 'scope': scope}
    return serializer.dumps(json_data, salt=current_app.config['SECRET_SALT'])


# 验证token
def verify_auth_token(token):

    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        original_data = serializer.loads(
            token,
            max_age=3 * 24 * 3600,
            salt=current_app.config['SECRET_SALT'])

        uid = original_data['uid']
        category = original_data['category']
        scope = original_data['scope']
        # return {uid: uid, category: category, scope: scope}
        return UserNamedTuple(uid=uid, category=category, scope=scope)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
