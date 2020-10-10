from flask import Blueprint

# 创建蓝图对象
home_blue = Blueprint('home_b',__name__)

# 让视图文件和主程序建立关联
from . import views