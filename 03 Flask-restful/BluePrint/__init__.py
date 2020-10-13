from flask import Blueprint
from flask_restful import Api
from .views import DemoResource
# 1.创建蓝图对象
home_blu = Blueprint('home_blue')

# 2.创建组件对象
home_api = Api(home_blu)

# 3.组件对象添加类视图
home_api.add_resource(DemoResource)