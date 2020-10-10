from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def deco1(f):

    def wrapper(*args, **kwargs):
        print('deco1')
        return f(*args, **kwargs)

    return wrapper

def deco2(f):

    def wrapper(*args, **kwargs):
        print('deco2')
        return f(*args, **kwargs)

    return wrapper


class DemoResource(Resource):
    # 通过method_decorators类属性设置装饰器
    # method_decorators = [deco1, deco2]  # 所有的请求方式都会添加这些装饰器
    method_decorators = {'get': [deco1], 'post': [deco2]}  # 可以指定请求方式对应的装饰器

    # @deco2
    # @deco1
    def get(self):

        return {'foo': "get"}

    def post(self):
        return {'foo': "post"}


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)
