from flask import Flask


app = Flask(__name__)

# 4.应用注册蓝图对象

from BluePrint import home_blu
app.register_blueprint(home_blu)


if __name__ == '__main__':
    app.run(port=8000, debug=True)



