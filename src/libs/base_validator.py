from flask import request
from wtforms import Form

from src.libs.error_code import ParameterException


class BaseForm(Form):

    def __init__(self):
        data = request.get_json(silent=True)
        kwargs = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **kwargs)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(self.errors)
        return self
