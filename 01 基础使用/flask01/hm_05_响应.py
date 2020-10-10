import json

from flask import Flask, make_response, Response, jsonify, redirect

app = Flask(__name__,  # 导入名称, flask会根据该参数查询静态文件夹
            # 官方建议使用__name__, 这样会从当前路径中查询静态文件夹
            # static_folder="static1",  # 设置静态文件的存储路径
            # static_url_path='/res/img' # 设置静态文件的URL访问路径 如 127.0.0.1:5000/res/img/213.png
            )

"""访问静态资源
1.将静态资源放入到 项目的 static 文件夹中
2.通过内置的静态资源的访问路由, URL路径格式为 /static/<filename>
"""

"""返回响应数据
1. 三个返回值    return 响应体, 状态码, 响应头
2. 自定义响应对象  
"""

# @app.route('/demo1')
# def demo1():
#     return 'hello flask', 400, {'A': 1}
#
#
# @app.route('/demo2')
# def demo2():
#     # 创建响应对象
#     response = make_response('hello flask')  # type: Response
#     response.status_code = 400  # 设置状态码
#     response.headers['B'] = 2  # 设置响应头
#
#     # 返回响应对象
#     return response


"""返回json"""

@app.route('/demo3')
def demo3():

    dict1 = {'name': 'zs', 'age': 20}
    # 可以将字典转为json字符串
    # data = json.dumps(dict1)
    # return data

    # jsonify()函数可以将字典转为json字符串, 并且自动设置响应头content-type:application/json
    # return jsonify(dict1)
    return jsonify(name='zs', age=20)  # 还支持关键字实参形式


"""重定向"""

@app.route('/demo4')
def demo4():
    # 重定向到指定的网站
    # return redirect('http://www.baidu.com')

    # 重定向到当前web应用的指定路由 只需要提供URL资源段即可
    return redirect('/demo3')


if __name__ == '__main__':
    # print(app.url_map)
    app.run(debug=True)
