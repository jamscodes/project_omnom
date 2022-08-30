from flask_app import app
from flask import render_template, request, redirect
from ..models.food import Food


@app.route('/meal/add-meal')
def r_add_meal():
    all_foods = Food.get_all()
    return render_template('add_meal.html', food_items = all_foods)


@app.route('/meal/add_meal', methods=['POST'])
def f_add_meal():
    for field in request.form:
        print(field)
    return redirect('/meal/add-meal')