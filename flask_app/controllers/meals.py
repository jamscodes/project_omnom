from flask_app import app
from flask import render_template, request, redirect
from ..models.food import Food
from ..models.meal import Meal


@app.route('/meal/add-meal')
def r_add_meal():
    all_foods = Food.get_all()
    return render_template('add_meal.html', food_items = all_foods)


@app.route('/meal/add_meal', methods=['POST'])
def f_add_meal():
    meal_data = {
        'name': request.form.get('meal_name'),
        'type': request.form.get('meal_type')
    }

    meal_id = Meal.add_meal(meal_data, request.form.getlist('food_items'))

    return redirect('/meal/add-meal')


@app.route('/meal/<int:meal_id>')
def r_show_meal(meal_id):
    meal_data = Meal.get_meal({'id': meal_id})

    return render_template('one_meal.html', meal = meal_data[0], ingredients = meal_data[1])