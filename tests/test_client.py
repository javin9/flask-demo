import enum


class ClientTypeEnum(enum.Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201


print(ClientTypeEnum(342))
