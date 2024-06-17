from flask import request, json
from werkzeug.exceptions import HTTPException


class APISuccess():
    code = 200
    msg = 'ok'
    error_code = 0

    def __init__(self, data=None, code=None, msg=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        self.data = data

    def get_body(self, environ=None, scope=None):
        body = dict(msg=self.msg,
                    code=self.code,
                    error_code=self.error_code,
                    data=self.data)
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None, scope=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

    def __init__(self,
                 msg=None,
                 code=None,
                 error_code=None,
                 headers=None,
                 data=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super().__init__(msg, None)

    def get_body(self, environ=None, scope=None):
        body = dict(msg=self.msg,
                    code=self.code,
                    error_code=self.error_code,
                    request=request.method + ' ' + self.get_url_no_param())
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None, scope=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
