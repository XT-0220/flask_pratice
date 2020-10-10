from flask import Flask, abort

# 01创建Flask应用
app = Flask(__name__)

@app.errorhandler(404)
def error_404(error):
    return 'error'


# 03 定义路由
# errorhandler不仅可以捕获http错误, 还可以捕获系统内置错误
@app.errorhandler(ZeroDivisionError)
def error_zero(error):
    return 'hello'


@app.route('/')
def index():
    abort(404)
    return 'index'


# 02运行应用
if __name__ == '__main__':
    app.run(port=8000, debug=True)

