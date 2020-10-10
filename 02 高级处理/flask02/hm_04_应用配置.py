from datetime import timedelta

from flask import Flask
from config import *

app = Flask(__name__)
# flask的配置可以通过config属性来进行设置
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)





# 从对象中加载配置  可以将配置封装成类, 减少重复的代码
app.config.from_object(DevelopmentConfig)


@app.route('/')
def index():
    # 获取应用配置
    print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    print(app.config.get('SQL_URL'))
    return "index"


if __name__ == '__main__':
    app.run(debug=True)
