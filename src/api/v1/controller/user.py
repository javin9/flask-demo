# from src.api.v1.blue_print import web_v1
from .. import web_v1


@web_v1.route('/user/list', methods=['GET'])
def get_user():
    return 'User'
