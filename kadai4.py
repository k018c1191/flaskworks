from flask import Flask, render_template

app = Flask(__name__)

u = []


@app.route('/user/<username>')
def uin(username):
    u.append(username)
    return render_template('kadai4.html', massage=username)

@app.route('/list/')
def list():
    return render_template('kadai4list.html', i=u)


if __name__ == '__main__':
    app.debug = True
    app.run()
