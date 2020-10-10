from flask import Flask

app = Flask(__name__)

# 通过环境变量来加载配置
app.config.from_envvar('ENV_CONFIG')


@app.route('/')
def index():
    print(app.config.get('SECRET_KEY'))
    return "index"


if __name__ == '__main__':
    app.run(debug=True)
