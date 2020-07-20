from flask import Flask

kadai1 = Flask(__name__)

@kadai1.route('/')

def top_page():
    return 'トップページ'

if __name__=='__main__':
    kadai1.debug = True
    kadai1.run()