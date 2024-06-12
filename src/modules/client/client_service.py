from flask import request
from src.enums.client import ClientTypeEnum
from src.libs.error_code import Success
from src.models.user import User
from src.models.base import db
from src.modules.client.client_validator import ClientForm, UserEmailForm


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
