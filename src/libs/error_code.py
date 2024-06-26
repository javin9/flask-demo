from werkzeug.exceptions import HTTPException

from src.libs.error import APIException


class Success(APIException):
    code = 0
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if msg:
            self.msg = msg
        super().__init__(msg, code, error_code, headers)


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if msg:
            self.msg = msg
        super().__init__(msg, code, error_code, headers)


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'

    def __init__(self, msg=None, code=None, error_code=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        super().__init__(msg, code, error_code)


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'
