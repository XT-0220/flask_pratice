from datetime import timedelta


class BaseConfig:
    """配置基类
    用于存放相同的配置, 对配置进行代码抽取
    """
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)


class DevelopmentConfig(BaseConfig):
    """开发环境配置
    在子类中实现各自不同的配置
    """
    SQL_URL = '127.0.0.1:5000/test1'


class ProductionConfig(BaseConfig):
    """生产环境"""

    SQL_URL = '192.168.105.140:5000/heima'


# 定义字典记录 配置类型 和 配置子类 的关系
config_dict = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig
}
