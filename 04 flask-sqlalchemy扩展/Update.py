from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 应用配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:970220@localhost:3306/test01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 方式1: 初始化组件对象, 直接关联Flask应用
db = SQLAlchemy(app)


# 构建模型类  类->表  类属性->字段  实例对象->记录
class Goods(db.Model):
    __tablename__ = 't_user'  # 设置表名, 表名默认为类名小写
    id = db.Column(db.Integer, primary_key=True)  # 设置主键, 默认自增
    name = db.Column('username', db.String(20), unique=True)  # 设置字段名 和 唯一约束
    age = db.Column(db.Integer, default=10, index=True)  # 设置默认值约束 和 索引


@app.route('/')
def Purchase():
    '''购买商品'''
    # 1. 查询过滤器 + 更新执行器, 进行数据更新
    Goods.query.filter(Goods.name =='方便面').update({'count':Goods.count -1})

    db.session.commit()

    return 'index'



if __name__ == '__main__':
    # 删除所有继承自db.Model的表
    db.drop_all()
    # 创建所有继承自db.Model的表
    db.create_all()
    app.run(debug=True)