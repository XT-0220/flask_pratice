from flask import Blueprint



# 1.创建蓝图对象
# 细节1: 可以通过url_prefix参数给蓝图定义的路由添加统一的资源段前缀, url_prefix='/home'
home_blu = Blueprint('home_b', __name__,url_prefix='/home')

from . import views

# 4.让视图文件和主程序建立关联
# ImportError: 一般都是导入的内容还未定义(循环导入问题)
# 解决办法: 查看并修改代码的执行顺序





# 细节3: 蓝图也可以设置请求钩子: 只有访问该蓝图定义的路由时才会触发
# @home_blu.before_request
# def home_prepare():
#     print('home_prepare')
