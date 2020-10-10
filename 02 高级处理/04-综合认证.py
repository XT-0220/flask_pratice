from flask import Flask, g, session

app = Flask(__name__)
app.secret_key='test'

@app.before_request
def prapare():
    g.name = session.get('username')


@app.route("/")
def index():
    if g.name:
        return 'welcome %s'%g.name
    else:
        return 'index'

@app.route('/login')
def login():
    session['username'] = 'zs'
    return 'login victory'

if __name__ == '__main__':
    app.run(port=8000, debug=True)

