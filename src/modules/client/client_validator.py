from wtforms import IntegerField, StringField, ValidationError, validators
from wtforms.validators import DataRequired, Length, Regexp

from src.enums.client import ClientTypeEnum
from src.libs.base_validator import BaseForm
from src.libs.error_code import ClientTypeError, ParameterException
from src.models.user import User

from email_validator import validate_email, EmailNotValidError


class ClientForm(BaseForm):
    # 账号
    account = StringField('account', validators=[DataRequired("账号不能为空")])
    # 密码
    secret = StringField('secret', validators=[])

    # 客户端类型
    category = IntegerField('category', validators=[DataRequired()])

    # 自定义验证器
    def validate_category(self, field):
        try:
            ClientTypeEnum(field.data)
        except ValueError as e:
            print(e)
            raise ClientTypeError()

        # self.category.data = client


class UserEmailForm(ClientForm):
    nickname = StringField('nickname',
                           validators=[DataRequired(),
                                       Length(min=2, max=22)])

    account = StringField('email', validators=[DataRequired()])

    def validate_account(self, field):
        try:
            email_information = validate_email(field.data,
                                               check_deliverability=False)
            email = email_information.normalized
            try:
                user = User.query.filter_by(email=email).first()
                if user:
                    raise ValidationError('用户已经存在')
            except ValidationError as e:
                raise e
        except EmailNotValidError as e:
            raise e

    # # 自定义验证器 校验用户是否存在
    # def validate_account(self, field):
    #     # field.data
    #     user = User.query.filter_by(email=field.data).first()
    #     if user:
    #         raise ValidationError('用户已经存在')

    # secret = StringField(
    #     'secret',
    #     validators=[DataRequired(),
    #                 Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    secret = StringField('secret', validators=[DataRequired()])
