from src.modules.client.client_service import create_client_service

from .. import web_v1


@web_v1.route('/client/register', methods=['POST'])
def create_client():
    return create_client_service()
