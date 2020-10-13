from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test35'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# 构建模型类
class Goods(db.Model):
    __tablename__ = 't_good'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    count = db.Column(db.Integer)


@app.route('/')
def purchase():

    goods = Goods(name='方便面', count=20)
    db.session.add(goods)

    db.session.flush()  # 手动执行数据库更新

    # Goods.query.all() # 查询时, 也会先执行flush操作
    # db.session.commit()  # 提交会话会自动执行flush操作

    return "index"


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    app.run(debug=True)
