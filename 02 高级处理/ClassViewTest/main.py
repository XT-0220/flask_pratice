from flask import Flask

app = Flask(__name__)

# 4.应用注册蓝图对象
from home import home_blu
app.register_blueprint(home_blu)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
