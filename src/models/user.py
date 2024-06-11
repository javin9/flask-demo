from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from src.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), nullable=False)
    auth = Column(SmallInteger, default=1)  # 1 普通用户 2 管理员 3 超级管理员

    # 对密码进行加密
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
