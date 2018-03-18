from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Bart_sucks!!!!!!!!!!'}
    return render_template('index.html', title="Whatever", user=user)