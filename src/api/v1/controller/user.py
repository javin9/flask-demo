# from src.api.v1.blue_print import web_v1
from src.models.user import User
from src.modules.user.user_service import delete_user_by_id
from .. import web_v1
from src.libs.token_auth import auth
from src.models.base import db
from flask import json, jsonify


@web_v1.route('/user/get/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user_model = User().query.filter_by(id=uid).first_or_404()
    return {"data": dict(user_model)}


@web_v1.route('/user/update', methods=['POST'])
@auth.login_required
def delete_user():
    return delete_user_by_id()


@web_v1.route('/super/get_user', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user_model = User().query.filter_by(id=uid).first_or_404()
    return {"data": dict(user_model)}
