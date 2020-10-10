# 请求钩子: 类比Django的中间件, 对请求的各阶段进行监听, 用于抽取视图中的公共代码, 减少代码冗余

from flask import Flask

app = Flask(__name__)

# 每次视图函数执行之前会调用, 一般会用于请求的准备工作, 如参数解析, 黑名单过滤, 数据统计等
# @app.before_request
# def prepare():
#     print('before_request')


# 没有出现错误的情况下, 每次视图函数执行之后调用, 一般会用于响应的加工工作, 如设置统一的响应头, 设置数据的外层包装
@app.after_request
def process(resp):  # 必须定义形参来接收响应对象

    resp.headers['A'] = 1
    print('after_request')
    return resp  # 加工完响应对象, 将响应对象再返回


# web应用被第一次请求时调用, 一般完成web应用初始化工作, 如数据库连接
@app.before_first_request
def initial():
    print('before_first_request')


# 每次视图函数执行之后调用, 无论是否出现异常都会执行, 一般进行请求的收尾工作, 如资源回收, 异常统计
@app.teardown_request
def clear_request(error):  # 必须定义形参接收具体的错误信息, 如果没有异常, error=None
    print('teardown_request: %s' % error)


# 设置请求钩子有两个语法形式: 装饰器 和 直接方法调用
# 直接方法调用的形式
def prepare():
    print('before_request')

app.before_request(prepare)


@app.route('/')
def index():
    print('执行视图')
    a = 1 / 0
    return "index"


if __name__ == '__main__':
    app.run()  # 想要测试teardown_request, 必须关闭调试模式
