from flask import render_template
from app import app

@app.route('/')
@app.route('/register')
def register():
    user = {'username' : 'Drive'}
    return render_template('register.html', title="Whatever tomorrow brings", user=user)