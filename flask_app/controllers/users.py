from flask_app import app
from flask import render_template, session
from flask_app.models.user import User

@app.route('/')
def r_login():
    return render_template('login.html')


@app.route('/dashboard')
def r_dashboard():
    session['user_id'] = 1

    user = User.get_one({'id': 1})

    return render_template('dashboard.html', user = user)