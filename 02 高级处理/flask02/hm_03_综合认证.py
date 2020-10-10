# 需求1: 获取用户身份信息   所有视图都需要获取
# 优化办法: 使用钩子函数获取用户信息, 再使用g变量来传递数据

from flask import Flask, session, g, abort
from functools import wraps

app = Flask(__name__)
app.secret_key = 'test'

@app.before_request
def get_userinfo():
    # 必须使用g变量记录用户信息, 如果使用全局变量则无法记录多个用户的数据
    g.name = session.get('username')


@app.route('/')
def index():
    if g.name:
        return "欢迎回来, %s" % g.name
    else:
        return '首页'




@app.route('/login')
def login():
    session['username'] = 'zs'
    return '登录成功'


# 需求2: 对指定的视图进行访问限制  部分视图的代码需要抽取
# 解决办法: 用装饰器封装身份校验逻辑, 需要访问限制的视图添加装饰器即可
def login_required(f):  # f=user

    # wraps的效果: 将被装饰函数(wrapper)的函数信息替换为指定函数(f)的函数信息 (如函数名)
    # wraps的使用场景: 只用于闭包函数, 目的避免闭包函数覆盖原函数信息
    # 添加该装饰器以后, 就不会有函数标记冲突的问题 (函数标记是根据函数名生成的, 如果不设置, 函数名都是使用的wrapper)

    @wraps(f)
    def wrapper(*args, **kwargs):

        # 通过__name__属性可以获取到函数名
        # print(wrapper.__name__)

        if g.name:  # 如果用户已登录, 正常访问视图

            return f(*args, **kwargs)  # user

        else:  # 如果用户未登录, 抛出401
            abort(401)

    return wrapper


@app.route('/user')
@login_required  # user = login_required(user)--->wrapper
def user():
    """个人中心"""
    # print(user.__name__)
    return '个人中心-%s' % g.name


@app.route('/demo1')
@login_required  # demo1 = login_required(demo1)--->wrapper
def demo1():
    return 'demo1'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True,port=8001)
