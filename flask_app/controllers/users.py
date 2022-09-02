from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.user import User
from flask_app.models.meal import Meal


@app.route('/')
def r_login():
    return render_template('login.html')


@app.route('/user/login', methods=['POST'])
def f_login():
    if User.validate_user_login(request.form):
        user = User.get_user_by_email({'email': request.form.get('email')})
        session['user_id'] = user.id
        return redirect('/dashboard')
    else:
        return redirect('/')


@app.route('/logout')
def p_logout():
    session.clear()
    return redirect('/')


@app.route('/dashboard')
def r_dashboard():
    user = User.get_user({'id': session['user_id']})

    all_meals = Meal.get_all_meals()

    return render_template('dashboard.html', user = user, meals = all_meals)