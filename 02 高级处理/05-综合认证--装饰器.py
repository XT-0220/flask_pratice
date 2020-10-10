from flask import Flask, g, session, abort

app = Flask(__name__)
app.secret_key='test'

@app.before_request
def prapare():
    g.name = session.get('username')


@app.route('/login')
def login():
    session['username'] = 'zs'
    return 'login victory'

def login_require(f):

    def wrapper(*args,**kwargs):
        if g.name:
            return f(*args,**kwargs)
        else:
            abort(401)
    return wrapper

@app.route('/user')
@login_require
def user():
    return '个人中心 %s ' %g.name


if __name__ == '__main__':
    app.run(port=8000, debug=True)

