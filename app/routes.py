from flask import render_template, request, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logan requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index')) #redirect to home page if username/password correct

    return render_template('login.html', title="Sign In", form=form)