

from flask import Flask,abort

app = Flask(__name__)

# http ：404 405 401
# 内置的异常类 Name  ZeroDivisionError

@app.errorhandler(404)
def error(error):
    return '这是一个404'

# 钩子
@app.before_request
def login_auth():
    pass

@app.after_request
def login_auth(resp):
    pass
    return  resp

@app.before_first_request
def login_auth():
    pass

@app.teardown_request
def login_auth(error):
    pass
    return  error


def login_auth():
    pass

app.before_request(login_auth)

# 范围： 有效的范围一次完整的请求，请求开始，请求结束   before_request  视图  after_request
# 请求上下文： request，session
# 应用上下文： g， : 1在请求的钩子和视图函数之间传递参数，2函数嵌套的时候
# current_app：相当于app的代理人，在不方便使用app的时候，可以使用current_app

@app.route("/")
def index():
    abort(401)
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)