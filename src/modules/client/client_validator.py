from wtforms import IntegerField, StringField, ValidationError, validators
from wtforms.validators import DataRequired, Length, Regexp, Email
from flask_wtf import FlaskForm

from src.enums.client import ClientTypeEnum
from src.models.user import User


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
    category = IntegerField('category', validators=[DataRequired()])

    # 自定义验证器
    def validate_category(self, field):
        try:
            ClientTypeEnum(field.data)
        except ValueError as e:
            raise e
        # raise ValueError('client type is wrong')


class UserEmailForm(ClientForm):
    nickname = StringField('nickname',
                           validators=[DataRequired(),
                                       Length(min=2, max=22)])

    account = StringField(
        'email',
        validators=[DataRequired(),
                    Email(message='invalidate email')])

    # 自定义验证器 校验用户是否存在
    def validate_account(self, field):
        # field.data
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('用户已经存在')

    secret = StringField(
        'secret',
        validators=[DataRequired(),
                    Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
