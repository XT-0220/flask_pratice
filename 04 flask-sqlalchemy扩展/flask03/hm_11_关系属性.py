from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import load_only

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test35'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

# 创建组件对象
db = SQLAlchemy(app)


# 用户表  主表(一)   一个用户可以有多个地址
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    addresses = db.relationship('Address')  # 1. 定义关系属性


# 地址表   从表(多)
class Address(db.Model):
    __tablename__ = 't_adr'
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(20))
    # 2.外键字段设置外键参数
    user_id = db.Column(db.Integer, db.ForeignKey('t_user.id'))


@app.route('/')
def index():
    """添加并关联数据"""

    user1 = User(name='张三')
    db.session.add(user1)
    db.session.flush()  # 需要手动执行flush操作, 让主表生成主键, 否则外键关联失败
    # db.session.commit()  # 有些场景下, 为了保证数据操作的原子性不能分成多个事务进行操作

    adr1 = Address(detail='中关村3号', user_id=user1.id)  # 2.让外键字段记录主表主键
    adr2 = Address(detail='华强北5号', user_id=user1.id)
    db.session.add_all([adr1, adr2])
    db.session.commit()

    return "index"

@app.route('/select')
def select():

    """需求: 查询姓名为张三的所有地址信息"""

    # 根据姓名查询主表数据
    user1 = User.query.filter(User.name == '张三').first()

    # # 根据外键匹配主表主键, 查询关联的地址数据
    adrs = Address.query.options(load_only(Address.detail)).filter_by(user_id=user1.id).all()
    for adr in adrs:
        print(adr.detail)

    # 3. 直接使用关系属性获取关联数据
    # for adr in user1.addresses:
    #     print(adr.detail)

    return 'select'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    app.run(debug=True)
