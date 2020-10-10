from flask import Flask

# 01创建Flask应用
app = Flask(__name__)

@app.before_request
def A():
    print('before_request')


@app.after_request
def B(resp):
    resp.headler['A'] = 1
    print('after_request')
    return resp



# 03 定义路由
@app.route("/")
def index():
    a = 1 / 10
    return 'hello'

# 02运行应用
if __name__ == '__main__':
    app.run(port=8000, debug=True)

