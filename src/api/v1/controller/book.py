from .. import web_v1


@web_v1.route('/book/list', methods=['GET'])
def get_book():
    return 'Book'
