from flask import Flask, render_template
from time import ctime
from utills import get_bitcoin_price

app = Flask(__name__)


@app.route('/news')
def news_page():
    return render_template("news_page.html")


@app.route('/')
def home_page():
    #bp = get_bitcoin_price()
    ct = ctime()

    return render_template('home_page.html', time=ct)#, bitcoin_price=bp, time=ct)


@app.route('/time')
def time_page():
    return render_template('time_page.html', my_current_time=ctime())


if __name__ == '__main__':
    app.run()
