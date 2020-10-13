from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)

# 1. 创建组件对象
api = Api(app)

# 2.定义类视图
class DemoResource(Resource):
    def get(self):
        return {'get':'foo'}
    def post(self):
        return {'post':'foo'}

# 3.添加类视图  函数标记默认为类名小写
api.add_resource(DemoResource, '/', endpoint='demo')

if __name__ == '__main__':
    app.run(port=8000, debug=True)

