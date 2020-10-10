# 上下文: 是数据容器, 记录了和Flask相关的各类数据
# 分类: 请求上下文, 应用上下文
# 共同特点: 有使用范围, 范围是:  [请求开始, 请求结束]  超出范围会报错
# 请求上下文: 记录请求有关的数据, request session
# 应用上下文: 记录应用有关的数据 current_app g

# g: flask给开发者预留的容器, 用于记录自定义数据, 每次请求记录的数据会重置
# 使用场景: 1> 在钩子函数和视图函数之间来传递数据  2> 函数嵌套调用可以用于传递数据

# current_app: 会自动引用创建的flask对象, 需要在项目的其他文件中使用flask对象时, 应该通过current_app来获取, 减少循环导入问题

from flask import Flask, request, g
from tool import func1

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    print(request.url)

    # 使用g变量记录数据
    g.name = name
    print(g.name)
    # 嵌套调用
    func1()
    return "index"


if __name__ == '__main__':
    # print(request.url)  # 超出使用范围, 会报错
    # print(g)  # 超出范围, 会报错
    app.run(debug=True,port=8000)
