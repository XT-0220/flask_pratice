# 蓝图作用: 实现Flask程序的模块化

from flask import Flask
from home import home_blu

app = Flask(__name__)


# 3.应用注册蓝图对象
app.register_blueprint(home_blu)


if __name__ == '__main__':
    # 细节2: 蓝图定义的路由, 其函数标记为: 蓝图名.函数名
    print(app.url_map)
    app.run(debug=True)
