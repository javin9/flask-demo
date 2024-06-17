import os
# 存放敏感的配置项
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/flask_restful_demo'

SECRET_KEY = os.urandom(32)
SECRET_SALT = 'tailiang'

MAX_AGE = 24 * 3600
