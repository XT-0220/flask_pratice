from home import home_blu

# 2.使用蓝图对象来定义路由
@home_blu.route('/user')  # 127.0.0.1:5000/home/
def index():
    return "index"





# @home_blu.route('/demo1')  # 127.0.0.1:5000/home/demo1
# def demo1():
#     return 'demo1'
