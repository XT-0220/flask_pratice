from flask import Flask, g
from tool import func1
app = Flask(__name__)


@app.route("/")
def index():
    g.name = 'zs'
    func1()
    return 'hello'

@app.route('/demo1')
def demo1():
    print(g.name)  # 会报错
    return 'demo1'

if __name__ == '__main__':
    app.run(port=8000, debug=True)

