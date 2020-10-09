from flask import Flask
# 01创建Flask应用
app = Flask(__name__)

# 03 定义路由
@app.route("/index", methods=['get', 'post'])
def index():

    return 'hello'

# 02运行应用
if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8000, debug=True)
    print(app.url_map)
    app.run(debug=True)
