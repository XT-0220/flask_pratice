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
class User(db.Model):
    __tablename__ = 't_user'  # 设置表名, 表名默认为类名小写
    id = db.Column(db.Integer, primary_key=True)  # 设置主键, 默认自增
    name = db.Column('username', db.String(20), unique=True)  # 设置字段名 和 唯一约束
    age = db.Column(db.Integer, default=10, index=True)  # 设置默认值约束 和 索引


@app.route('/')
def index():
    """增加数据"""

    # 1.创建模型对象
    user1 = User(name='zs', age=20)
    # user1.name = 'zs'
    # user1.age = 20

    # 2.将模型对象添加到会话中
    db.session.add(user1)
    # 添加多条记录
    # db.session.add_all([user1, user2, user3])

    # 3.提交会话 (会提交事务)
    # sqlalchemy会自动创建隐式事务
    # 事务失败会自动回滚
    db.session.commit()

    return "index"


if __name__ == '__main__':
    # 删除所有继承自db.Model的表
    db.drop_all()
    # 创建所有继承自db.Model的表
    db.create_all()
    app.run(debug=True)