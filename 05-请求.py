from flask import Flask, request

# 01创建Flask应用
app = Flask(__name__)

# 03 定义路由
@app.route("/",methods=['get', 'post'])
def index():
    # 1.url
    print(request.url)
    # 2.本次请求方式
    print(request.method)
    # 3.请求头  类字典对象
    print(request.headers)
    # 4.根据键值对
    print(request.headers['host'])
    # 5.键不存在不报错
    print(request.headers.get('host'))
    # 6.获取查询字符串   类对象   xx?name=zs&age=20
    print(request.args.get('name'))
    print(request.args.get('age'))
    # 7.请求体  表单   文本 (json/xml)  文件
    # 获取表单数据   request.form  类字典对象
    print(request.form.get('username'))
    # 获取文本数据   request.data   request.json
    print(request.data)   #bytes
    print(request.json.get('score'))






    return 'hello'






















# 02运行应用
if __name__ == '__main__':
    app.run(port=8000, debug=True)

