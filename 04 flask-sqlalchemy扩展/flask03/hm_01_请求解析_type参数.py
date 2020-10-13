import re

from flask import Flask
from flask_restful import Resource, Api
from flask_restful.inputs import boolean, date, datetime_from_iso8601, int_range, regex
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app)


# 自定义函数: 既可以进行参数校验, 也可以进行格式转换   正确格式如:   user:123213213
def func1(value):  # 必须定义形参接收原始参数
    if re.match(r'^user:', value):
        return value[5:]
    else:
        raise ValueError('age参数格式错误')  # 该类型的错误信息会自动包装为json形式返回


class DemoResource(Resource):
    def get(self):
        # 创建解析器
        parser = RequestParser()

        # 添加参数规则
        # parser.add_argument('age', type=int)  # 转为int类型

        # parser.add_argument('age', type=boolean)  # 转为bool类型   1/0 true/false
        # parser.add_argument('age', type=date)  # 日期 转为datetime类型   YYYY-mm-dd
        # parser.add_argument('age', type=datetime_from_iso8601)  # 时间 转为datetime类型  2012-01-01T23:30:00+02:00
        # parser.add_argument('age', type=int_range(5, 10))  # 转为int类型 限定范围[5, 10]

        # parser.add_argument('age', type=regex(r'^1[3-9]\d{9}$'))  # 只进行格式校验

        # 自定义函数
        parser.add_argument('age', type=func1)  # 自定义函数

        # 执行解析
        args = parser.parse_args()

        # 获取参数
        print(args.age)
        print(type((args.age)))

        return {'foo': "get"}

    def post(self):
        return {'foo': "post"}


api.add_resource(DemoResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
