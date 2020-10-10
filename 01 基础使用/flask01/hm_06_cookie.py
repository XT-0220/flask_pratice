from flask import Flask, make_response, Response, request

app = Flask(__name__)


@app.route('/')
def index():
    # 后端设置cookie数据: 通过响应头的set_cookie字段

    # 创建响应对象
    response = make_response('index')  # type: Response
    # 设置cookie数据  value必须是str/bytes
    response.set_cookie('per_page', '10', max_age=86400)

    # 删除cookie  本质就是设置max-age=0
    # response.delete_cookie('per_page')
    return response


@app.route('/demo1')
def demo1():

    # 获取cookie数据: 浏览器会自动通过请求头将cookie数据发给服务器
    # request.cookies 可以直接获取到字典形式的cookie数据
    print(request.cookies.get('per_page'))

    return 'demo1'


if __name__ == '__main__':
    app.run(debug=True)
