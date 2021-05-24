from os import close
from flask import Flask, render_template, request
import mysql.connector
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://chip:123@localhost/vitbcwc ctf'
db = SQLAlchemy(app)


class Register_db(db.Model):

    '''
    id,name registration no email password
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    registration_no = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=True)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        name = request.form.get('name')
        registration_no = request.form.get('registration_no')
        email = request.form.get('email')
        password = request.form.get('password')

        entry = Register_db(
            name=name, registration_no=registration_no, email=email, password=password)
        db.session.add(entry)
        db.session.commit()
    return render_template('register.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login_validation', methods=['POST', 'GET'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    return "The email is {} and the password is{}".format(email, password)


if __name__ == "__main__":
    app.run(debug=True)
