from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    # print(request.url)  # url
    # print(request.method)  # 本次请求方式
    # print(request.headers)  # 请求头  类字典对象

    # print(request.headers['Host'])  # 根据键取值
    # print(request.headers.get('Host'))  # 键不存在不报错

    # 请求传递数据 1> URL路径 -> 路由变量  2> 查询字符串 get  3> 请求体  post  4> 请求头 -> request.headers

    # 获取查询字符串 request.args  类字典对象  xx?name=zs&age=20
    # print(request.args.get('name'))
    # print(request.args.get('age'))

    # 请求体  表单  文本(json/xml)  文件(图片)

    # 获取表单数据  request.form  类字典对象
    # print(request.form.get('username'))

    # 获取文本数据  request.data/request.json
    # print(request.data)  # bytes类型
    # print(request.json.get('score'))  # 会将获取的json字符串直接转为字典

    # 获取文件数据  request.files  类字典对象
    file = request.files.get('avatar')  # 获取的是文件对象

    # 可以保存到本地
    # file.save('213.png')

    # 读取上传的二进制数据
    file_bytes = file.read()
    print(file_bytes)

    return "index"


if __name__ == '__main__':
    app.run(debug=True)
