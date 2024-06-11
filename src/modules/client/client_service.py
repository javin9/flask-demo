from flask import request
from src.enums.client import ClientTypeEnum
from src.models.user import User
from src.models.base import db
from src.modules.client.client_validator import ClientForm, UserEmailForm


def create_client_service():
    form = ClientForm(data=request.json)
    if form.validate():
        return _resister_switch(form.category.data)


def _resister_switch(category):
    return {
        ClientTypeEnum.USER_EMAIL: _register_user_by_email,
        ClientTypeEnum.USER_MOBILE: _register_user_by_mobile,
    }[category]()


def _register_user_by_email():
    form = UserEmailForm(data=request.json)
    with db.auto_commit():
        user = User()
        user.nickname = form.nickname.data
        user.email = form.account.data
        user.password = form.secret.data
        db.session.add(user)


def _register_user_by_mobile():
    pass
