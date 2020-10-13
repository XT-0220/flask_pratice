from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test35'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 创建组件对象
db = SQLAlchemy(app)


# 构建模型类  商品表
class Goods(db.Model):
    __tablename__ = 't_good'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    count = db.Column(db.Integer)


@app.route('/')
def purchase():
    """购买商品"""

    # 更新方式2: update子查询   可以避免更新丢失问题
    # update t_good set count = count - 1 where name = '方便面';

    # 1. 查询过滤器 + 更新执行器, 进行数据更新
    Goods.query.filter(Goods.name == '方便面').update({'count': Goods.count - 1})

    # 2. 提交会话
    db.session.commit()

    return "index"


if __name__ == '__main__':
    # 重置数据库数据
    db.drop_all()
    db.create_all()

    # 添加一条测试数据
    goods = Goods(name='方便面', count=1)
    db.session.add(goods)
    db.session.commit()
    app.run(debug=True)
