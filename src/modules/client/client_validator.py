from wtforms import IntegerField, StringField, validators
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

from src.enums.client import ClientTypeEnum


class ClientForm(FlaskForm):
    # 账号
    account = StringField('account',
                          validators=[
                              DataRequired(),
                              Length(min=6,
                                     max=20,
                                     message="字符个数需要在{}和{}之间".format(5, 30))
                          ])
    # 密码
    secret = StringField('secret', validators=[])

    # 客户端类型
    # https://wtforms.readthedocs.io/en/3.1.x/validators/#custom-validators
    category = IntegerField('category', validators=[DataRequired()])

    # 自定义验证器
    def validate_category(self, field):
        try:
            ClientTypeEnum(field.data)
        except ValueError as e:
            raise e
        # raise ValueError('client type is wrong')
