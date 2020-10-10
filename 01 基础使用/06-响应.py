from flask import Flask, jsonify, redirect
from flask import make_response, Response

# 01创建Flask应用
app = Flask(__name__,  # 导入名称, flask会根据该参数查询静态文件夹
            # 官方建议使用__name__, 这样会从当前路径中查询静态文件夹
            # static_folder="static1",  # 设置静态文件的存储路径
            # static_url_path='/res/img' # 设置静态文件的URL访问路径 如 127.0.0.1:5000/res/img/213.png
            )
"""
访问静态资源
1.将静态资源放入到 项目的 static 文件夹中
2.通过内置的静态资源的访问路由, URL路径格式为 /static/<filename>
"""

# ====================================================

"""
返回响应数据
1. 三个返回值    return 响应体, 状态码, 响应头
2. 自定义响应对象  
"""

# 03 定义路由
@app.route("/index")
def index():
    return 'hello', 400, {'A':1}

@app.route('/index2')
def index2():
    # 创建响应对象
    response = make_response('hello')
    response.status = 400
    response.headers['B']=2
    return response

# ================================================================

'''返回json'''

@app.route('/index3')
def index3():

    dict1 = {'name': 'zs', 'age': 20}
    # 字典转json字符串
    # return json.dumps(dict1)

    # 可以将字典转json字符串, 并且设置响应头的content-type为application/json
    # return jsonify(dict1)
    return jsonify(name='zs', age=20)  # 也支持关键字实参的形式

# ====================================================================

'''重定向'''
@app.route('/index4')
def index4():
    # 重定向到指定网站
    # return redirect('http://www.baidu.com')
    # 重定向到当前web应用的指定路由
    return redirect('/index3')


# 02运行应用
if __name__ == '__main__':
    app.run( port=8000, debug=True)

