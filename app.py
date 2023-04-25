from flask import Flask, render_template
from time import ctime

app = Flask(__name__)


@app.route('/news')
def news_page():
    return render_template("news_page.html")


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/time')
def time_page():
    return render_template('time_page.html', my_current_time = ctime())


if __name__ == '__main__':
    app.run()
