# from flask import Flask
# # 01创建Flask应用
# app = Flask(__name__)
#
# # 03 定义路由
# @app.route("/user/<int:userid>")
# def index(userid):
#     print(userid)
#     return 'hello'
#
# # 02运行应用
# if __name__ == '__main__':
#     app.run(port=8000, debug=True)

# --------------------------------------------------------
# 自定义转换器
from flask import Flask
from werkzeug.routing import BaseConverter
# 01创建Flask应用
app = Flask(__name__)

# 1. 定义转换器类, 继承BaseConverter
class MobileConverter(BaseConverter):
    # 2. 设置regex属性, 指定匹配规则
    regex = r'1[3-9]\d{9}$'

# 3.应用添加自定义转换器
app.url_map.converters['mob'] = MobileConverter

@app.route("/index/<mob:mobile>")
def index(mobile):
    print(mobile)
    return 'hello'

# 02运行应用
if __name__ == '__main__':
    print(app.url_map.converters)
    app.run(port=8000, debug=True)


