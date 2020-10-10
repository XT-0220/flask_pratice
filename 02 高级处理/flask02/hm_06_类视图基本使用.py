from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

# 1.创建组件对象
api = Api(app)


# 2.定义类视图 继承Resource
class DemoResource(Resource):
    def get(self):
        # 类视图的content-type默认变为json形式
        # 类视图可以直接返回字典, 会自动包装为json字符串
        return {'get': 'foo'}

    def post(self):
        return {'post': 'foo'}


# 3.添加类视图  函数标记默认为类名小写
api.add_resource(DemoResource, '/', endpoint='demo')


# @app.route('/')
# def index():
#
#     return "index"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
