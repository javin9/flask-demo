from wtforms import IntegerField
from src.libs.base_validator import BaseForm
from wtforms.validators import DataRequired, Length, Regexp


class UserDeleteForm(BaseForm):
    uid = IntegerField('uid', validators=[DataRequired("用户id不能为空")])
