from functools import wraps

from flask import Flask, g, session, abort

app = Flask(__name__)
app.secret_key='test'

@app.before_request
def prapare():
    g.name = session.get('username')


@app.route('/login')
def login():
    session['username'] = 'zs'
    return 'login victory'

# 装饰器函数
def login_require(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if g.name:
            return f(*args,**kwargs)
        else:
            abort(401)
    return wrapper

# 使用装饰器
@app.route('/user')
@login_require
def user():
    return '个人中心 %s ' % g.name

@app.route('/user')
@login_require
def demo1():
    return demo1


if __name__ == '__main__':
    app.run(port=8000, debug=True)

