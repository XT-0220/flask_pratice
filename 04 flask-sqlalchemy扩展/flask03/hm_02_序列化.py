from flask import Flask
from flask_restful import Resource, Api, marshal, fields, marshal_with

app = Flask(__name__)
api = Api(app)

class User:  # 定义模型类
    def __init__(self):
        self.name = 'zs'
        self.age = 20
        self.height = 1.8
        self.scores = [80, 90]
        self.info = {
            'gender': True
        }

    def to_dict(self):
        """自定义方法 将模型转为字典"""
        return {
            'name': self.name,
            'height': self.height
        }


fields = {  # 序列化规则
    'username': fields.String(attribute='name'), # 指定对应的模型属性
    'age': fields.Integer(default=10),  # 设置默认值
    'height': fields.Float,
    'scores': fields.List(fields.Integer),  # 元素类型唯一
    'info': fields.Nested({'gender': fields.Boolean})
}


class DemoResource(Resource):
    method_decorators = {'post': [marshal_with(fields)]}

    def get(self):

        user1 = User()

        # marshal函数可以按照指定的序列化规则将 模型对象 转为 字典
        # envelope参数可以对序列化数据进行外层包装
        return marshal(user1, fields, envelope='data')

    def post(self):

        user1 = User()
        # 如果使用了marshal_with装饰器, 则可以直接返回模型对象
        return user1

    def put(self):
        user1 = User()
        return user1.to_dict()


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)
