from src.enums.client import ClientTypeEnum


def resister_switch(form):
    promise = {
        ClientTypeEnum.USER_EMAIL: _register_user_by_email,
        ClientTypeEnum.USER_MOBILE: _register_user_by_mobile,
    }


def _register_user_by_email():
    pass


def _register_user_by_mobile():
    pass
