from datetime import timedelta

from flask import Flask, session

app = Flask(__name__)
# 设置应用秘钥
app.secret_key = 'test'
# 修改session的过期时间
app.permanent_session_lifetime = timedelta(days=7)


@app.route('/')
def index():
    # session是一个类字典对象, 只要对其取值/赋值就可以完成session数据的读写

    # 记录session数据
    session['username'] = 'zs'

    # 设置session支持过期时间  默认为31天
    session.permanent = True

    # 删除session数据
    # session.pop('username')

    return "index"


@app.route('/demo1')
def demo1():
    # 获取session数据
    print(session.get('username'))

    return 'demo1'


if __name__ == '__main__':
    app.run(debug=True)
