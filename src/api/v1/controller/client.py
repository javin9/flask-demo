from src.modules.client.client_service import create_client_service, get_token_service

from .. import web_v1


@web_v1.route('/client/register', methods=['POST'])
def create_client():
    return create_client_service()


@web_v1.route('/client/get_token', methods=['POST'])
def get_token():
    return get_token_service()
