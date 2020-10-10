# 路由变量: 传递URL参数

# from flask import Flask
#
# app = Flask(__name__)

# # 格式: /xx/<路由变量名>
# @app.route('/user/<userid>')
# def index(userid):  # 必须定义同名形参接收路由变量的值
#     print(userid)
#     return "index"
#


"""路由转换器"""

# from flask import Flask
#
# app = Flask(__name__)

# # 路由转换器: URL参数进行格式校验, 如果不匹配则返回404
# # 格式: /xx/<转换器名:路由变量名>
# @app.route('/user/<int:userid>')  # 要求userid必须是1-n个整数
# def index(userid):
#     print(userid)
#     return "index"


"""自定义转换器"""
from werkzeug.routing import BaseConverter

from flask import Flask

app = Flask(__name__)


# 1. 定义转换器类, 继承BaseConverter
class MobileConverter(BaseConverter):
    # 2.设置regex属性, 指定匹配规则
    regex = r'1[3-9]\d{9}$'  # 不要加开头的^


# 3.应用添加自定义转换器
app.url_map.converters['mob'] = MobileConverter


@app.route('/demo1/<mob:mobile>')   # 使用自定义转换器
def demo1(mobile):
    print(mobile)
    return 'demo1'


if __name__ == '__main__':
    # 查看所有转换器  {转换器名: 转换器类}
    # print(app.url_map.converters)
    app.run(debug=True)
