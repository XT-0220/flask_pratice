# flask对http错误进行了封装, 可以捕获http错误, 也可以主动抛出
from flask import Flask, abort

app = Flask(__name__)


@app.errorhandler(404)
def error_404(error):  # 一旦捕获异常, 必须定义形参接收具体的错误信息

    return '<h3>您访问的页面去浪迹天涯了, %s </h3> ' % error

# errorhandler不仅可以捕获http错误, 还可以捕获系统内置错误
@app.errorhandler(ZeroDivisionError)
def error_zero(error):
    return '除数不能为0'


@app.route('/')
def index():
    # a = 1 / 0

    # 主动抛出http错误
    abort(404)
    return "index"


if __name__ == '__main__':
    app.run(debug=True)
