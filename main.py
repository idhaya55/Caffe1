from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', 'sqlite:///cafes.db')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet =  db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/cafes')
def hello():
    post = Cafe.query.all()
    print(post[0].name)
    return render_template('main.html', filt=post)

@app.route('/cafe/<int:id>')
def cafe(id):
    cafe = Cafe.query.get(id)
    return render_template('cafes.html', tilt=cafe)
if '__main__' == __name__:
    app.run(debug=True)
