from src.app import create_app
from src.libs.error import APIException
from src.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        code = e.code
        msg = e.description or e.msg
        error_code = e.error_code or 500
        return APIException(msg=msg, code=code, error_code=error_code)
    else:
        if not app.config["DEBUG"]:
            return ServerError()
        else:
            raise e


if __name__ == "__main__":
    app.run(debug=True, port=3333)
