from flask import Flask,make_response,Response,request
# 01创建Flask应用
app = Flask(__name__)

# 03 定义路由
@app.route("/")
def index():
    # 后端设置cookie数据, 通过set_cookie
    # 创建响应对象
    response = make_response('index')
    # 删除cookie , 本质就是设置max-age=0
    response.delete_cookie('per_page')
    return response

@app.route('/index2')
def index2():
    print(request.cookies.get('per_page'))
    return 'hello'

# 02运行应用
if __name__ == '__main__':
    app.run(port=8000, debug=True)

