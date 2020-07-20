from flask import Flask
import datetime
import calendar

kadai2 = Flask(__name__)

@kadai2.route('/')
def top_page():
    dt = datetime.datetime.now()
    strdt = dt.strftime('%m/%d %H:%M')
    return strdt


if __name__ == '__main__':
    kadai2.debug = True
    kadai2.run()
