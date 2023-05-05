from flask import Flask, render_template
from time import ctime
from utils import get_bitcoin_price

app = Flask(__name__)


@app.route('/news')
def news_page():
    return render_template("news_page.html")


@app.route('/weather')
def weather_page():
    return render_template("weather_page.html")


@app.route('/')
def home_page():
    bp = get_bitcoin_price()
    ct = ctime()

    return render_template('home_page.html', bitcoin_price=bp, time=ct)


@app.route('/time')
def time_page():
    return render_template('time_page.html', my_current_time=ctime())


@app.route('/contact')
def contact_page():
    return render_template('contact_page.html')


@app.route('/exit')
def exit_page():
    return render_template('exit_page.html')


if __name__ == '__main__':
    app.run()
