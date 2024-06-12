from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from src.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(128), unique=True, nullable=False)
    nickname = Column(String(128), nullable=False)
    auth = Column(SmallInteger, default=1)  # 1 普通用户 2 管理员 3 超级管理员
    category = Column(Integer, nullable=False)  # 100 邮箱注册 101 手机注册 103 微信注册

    # 对密码进行加密
    _password = Column('password', String(128), nullable=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = raw  # generate_password_hash(raw) 加密，暂时去掉
