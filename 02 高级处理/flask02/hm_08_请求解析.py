from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app)


class DemoResource(Resource):
    def get(self):
        # 1.创建请求解析器
        parser = RequestParser()

        # 2.添加参数规则
        parser.add_argument('name')
        parser.add_argument('age')

        # 3.执行解析 默认会解析 查询字符串/form表单/json数据
        args = parser.parse_args()

        # 4.获取参数
        print(args.name)
        print(args.age)

        return {'foo': "get"}

    def post(self):
        # 1.创建请求解析器
        parser = RequestParser()

        # 2.添加参数规则
        # 要求该参数必须传递, 否则返回400
        # 从json字符串中提取数据
        parser.add_argument('name', required=True, location='json')
        # 如果age未传递,使用默认值
        parser.add_argument('age', default=10)

        # 3.执行解析 默认会解析 查询字符串/form表单/json数据
        args = parser.parse_args()

        # 4.获取参数
        print(args.name)
        print(args.age)
        return {'foo': "post"}


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)
