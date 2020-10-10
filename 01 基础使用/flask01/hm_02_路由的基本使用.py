from flask import Flask

app = Flask(__name__)


# 细节1: URL资源段必须以/开头
# 细节3: 可以通过app.route()的methods参数设置路由支持的请求方式
@app.route('/hello', methods=['get', 'post'])
def index():

    return "index"


if __name__ == '__main__':
    # 细节2: 通过app.url_map查看所有的路由规则
    print(app.url_map)
    app.run(debug=True)
