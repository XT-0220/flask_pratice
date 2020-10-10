from flask import Flask

# 1. 创建Flask应用
app = Flask(__name__)


# 3. 定义路由
@app.route('/')
def index():
    a = 1 / 10
    return 'hello flask'


if __name__ == '__main__':
    # 2. 运行应用 (启动一个测试服务器, 接收请求并调用对应的视图函数)
    # host: 绑定的ip地址  0.0.0.0
    # port: 监听的端口
    # debug: 是否开启调试模式 1> python错误会直接显示在网页上 2> 代码更新后, 测试服务器会自动重启
    # app.run(host='0.0.0.0', port=8000, debug=True)
    pass
