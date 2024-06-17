from src.libs.error_code import DeleteSuccess, Success
from src.models.user import User
from src.modules.user.user_validator import UserDeleteForm
from src.models.base import db


def delete_user_by_id():
    form = UserDeleteForm().validate_for_api()
    with db.auto_commit():
        User().query.filter_by(id=form.uid.data).update({"status": 0})
    return DeleteSuccess()
