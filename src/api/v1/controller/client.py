from flask import request

from src.modules.client.client_validator import ClientForm
from .. import web_v1


@web_v1.route('/register', methods=['POST'])
def create_client():
    json_data = request.get_json()
    form = ClientForm(data=json_data)
    # 注册 登录
    # 接受参数 校验
    if form.validate():
        pass
