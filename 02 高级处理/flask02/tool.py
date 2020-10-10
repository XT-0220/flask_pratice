from flask import g, current_app


def func1():
    print('func1')
    print(g.name)

    # 使用current_app代替app
    print(current_app.url_map)
    # func2()
