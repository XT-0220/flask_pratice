from json import dumps


from flask import Flask, current_app, make_response
from flask_restful import Resource, Api
from six import PY3

app = Flask(__name__)
api = Api(app)


# @api.representation('application/json')  # 设置json形式的自定义转换函数
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    settings = current_app.config.get('RESTFUL_JSON', {})

    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    """对响应字典进行外层包装"""
    if 'message' not in data:  # 如果视图自定义了错误信息, 则不再添加默认的外层包装
        data = {
            'data': data,
            'message': 'ok'
        }

    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp

# 也可以将装饰器展开, 直接调用方法(实际开发中会减少重复代码)
api.representation('application/json')(output_json)


class DemoResource(Resource):
    def get(self):

        return {'foo': "get"}

    def post(self):

        # 假设前端传递的参数错误, 需要在视图中自己构建错误信息
        return {'message': "param error", 'data': None}


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)
