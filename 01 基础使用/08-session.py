from datetime import timedelta
import redis as redis
from flask import Flask, session
from flask_session import Session


# 01创建Flask应用
app = Flask(__name__)
# 设置应用秘钥
app.secret_key = 'test'
# 修改session的过期时间
app.permanent_session_lifetime = timedelta(days=7)
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SINCE'] = False
app.config['SESSION_KEY_PREFIX'] = 'session'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379')

Session(app)



# 03 定义路由
@app.route("/")
def index():
    # 记录session数据
    session['username'] = 'zs'

    # 设置session支持过期时间
    session.permanent = True

    # 删除session数据
    # session.pop('username')

    return 'hello'

@app.route('/index2')
def index2():
    # 获取session数据
    print(session.get('username'))
    return 'hello'



# 02运行应用
if __name__ == '__main__':
    app.run(port=8000, debug=True)

