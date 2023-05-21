from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request
from time import ctime
from utils import get_bitcoin_price, get_news
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.id}"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<users {self.id}"


@app.route('/')
def index():
    return render_template('index.html', title="Glavnaya")


@app.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == "POST":
        try:
            hash = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], psw=hash)
            db.session.add(u)
            db.session.flush()

            p = Profiles(name=request.form['name'], old=request.form['old'],
                         city=request.form['city'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")
    return render_template('register_page.html', title="Registration")


@app.route('/news')
def news():
    news_data = get_news('2a0c54798f53408c94817e8606ba5d2a')
    return render_template('news_page.html', news=news_data)


@app.route('/weather')
def weather_page():
    return render_template("weather_page.html")


@app.route('/home_page')
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
    app.run(debug=True)
