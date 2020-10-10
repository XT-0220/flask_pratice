from home import home_blue

# 使用蓝图对象来定义路由
@home_blue.route('/')
def index():
    return 'index'