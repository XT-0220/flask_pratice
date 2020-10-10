from flask import Flask, current_app
from config import config_dict

# 工厂函数: 根据参数需求, 将对象创建的创建过程封装起来
def create_app(config_type):
    """封装应用的创建过程"""

    # 创建flask对象
    flask_app = Flask(__name__)

    # 根据配置类型取出配置子类
    config_class = config_dict[config_type]

    # 先加载普通配置
    flask_app.config.from_object(config_class)

    # 再加载隐私配置 (实现覆盖的关系)
    # 设置silent=True, 即使配置加载失败也不报错
    flask_app.config.from_envvar('ENV_CONFIG', silent=True)

    # 添加路由
    flask_app.add_url_rule('/', index.__name__, index)

    # 注册蓝图对象
    # flask_app.register_blueprint(home_blu)

    return flask_app


def index():
    print(current_app.config.get('PERMANENT_SESSION_LIFETIME'))
    print(current_app.config.get('SQL_URL'))

    return "index"

"""动态创建应用, 则代码中写死的app是失效的"""

# 创建应用
# app = create_app('pro')


# @app.route('/')
# def index():
    # print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    # print(app.config.get('SQL_URL'))

    # return "index"




# if __name__ == '__main__':
#     app.run(debug=True)
