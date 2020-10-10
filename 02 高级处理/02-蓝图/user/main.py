from flask import Flask
from home import home_blue


app = Flask(__name__)

# 应用注册蓝图对象
app.register_blueprint(home_blue)

if __name__ == '__main__':
    app.run(debug=True)

