from flask import Flask, render_template, request

app = Flask(__name__)

steps = []


@app.route('/')
def index():
    return render_template('kadai5-1index.html')


@app.route('/send', methods=['POST'])
def send():
    name = request.form.get('name')
    email = request.form.get('email')
    if name is None:
        name = ''
        email = ''
    return render_template('kadai5-1receive.html', name=name, email=email)


if __name__ == '__main__':
    app.debug = True
    app.run()
