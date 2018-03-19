from flask import render_template, request
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index', methods= ['GET', 'POST'])
def index():
    data = request.form
    print('from data', data)
    user = {'username' : 'Kailua'}
    return render_template('index.html', title="Whatever", user=user)
@app.route('/register')
def register():
    return render_template('register.html', title="Registration")

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)