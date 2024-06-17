from flask import request, current_app, jsonify
from itsdangerous import URLSafeTimedSerializer
from src.enums.client import ClientTypeEnum
from src.libs.error_code import NotFound, ParameterException, Success
from src.libs.token_auth import generate_auth_token
from src.models.user import User
from src.models.base import db
from src.modules.client.client_validator import ClientForm, UserEmailForm
from werkzeug.security import check_password_hash


def create_client_service():
    # form = ClientForm(data=request.json)
    # print(form.category.data, form.validate())
    # if form.validate():
    #     return _resister_switch(ClientTypeEnum(form.category.data))

    form = ClientForm().validate_for_api()
    print(form.category.data)
    return _resister_switch(ClientTypeEnum(form.category.data))


def _resister_switch(category):
    switch_map = {
        ClientTypeEnum.USER_EMAIL: _register_user_by_email,
        ClientTypeEnum.USER_MOBILE: _register_user_by_mobile,
    }
    switch_map[category]()
    return Success()


# 通过邮件方式注册
def _register_user_by_email():
    form = UserEmailForm().validate_for_api()
    with db.auto_commit():
        user = User()
        user.nickname = form.nickname.data
        user.email = form.account.data
        user.password = form.secret.data
        user.category = form.category.data
        db.session.add(user)


# 通过手机号方式注册
def _register_user_by_mobile():
    pass


def get_token_service():
    form = ClientForm().validate_for_api()
    user = User.query.filter_by(email=form.account.data).first_or_404()
    if not user:
        raise NotFound(msg='用户不存在')
    if not user.password:
        raise NotFound(msg='用户密码错误')
    if not check_password_hash(user.password, form.secret.data):
        raise ParameterException(msg='用户密码错误2')
    scope = 'AdminScope' if user.auth == 2 else 'UserScope'

    token = generate_auth_token(uid=user.id,
                                category=form.category.data,
                                scope=scope)
    json_data = {"token": token}
    return jsonify(json_data), 201
