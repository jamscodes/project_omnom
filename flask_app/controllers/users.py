from flask_app import app
from flask import render_template, session, redirect
from flask_app.models.user import User
from flask_app.models.meal import Meal


@app.route('/')
def r_login():
    return render_template('login.html')


@app.route('/logout')
def p_logout():
    session.clear()
    print(session)
    return redirect('/')


@app.route('/dashboard')
def r_dashboard():
    session['user_id'] = 1

    user = User.get_user({'id': 1})

    all_meals = Meal.get_all_meals()

    return render_template('dashboard.html', user = user, meals = all_meals)