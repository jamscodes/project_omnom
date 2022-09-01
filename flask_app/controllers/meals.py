from flask_app import app
from flask import render_template, request, redirect, session
from ..models.food import Food
from ..models.meal import Meal


@app.route('/meal/add-meal')
def r_add_meal():
    all_foods = Food.get_all()
    return render_template('add_meal.html', food_items = all_foods)


@app.route('/meal/add_meal', methods=['POST'])
def f_add_meal():
    session['meal_data'] = {
        'name': request.form.get('meal_name'),
        'type': request.form.get('meal_type'),
        'ingredients': request.form.getlist('food_items')
    }

    ingredients = []

    for ingredient in session['meal_data']['ingredients']:
        ingredients.append(Food.get_food({'id': ingredient}))

    return render_template('add_meal_quantities.html', ingredients = ingredients)


@app.route('/meal/add_ingredient_quantities', methods=['POST'])
def f_finish_meal():
    meal_data = {
        'name': session['meal_data']['name'],
        'type': session['meal_data']['type']
    }

    quantities_list = []

    for input in request.form:
        quantities_list.append(request.form.get(input))

    ingredient_data = {
        'ids': session['meal_data']['ingredients'],
        'quantities': quantities_list
    }

    Meal.add_meal(meal_data, ingredient_data)

    return redirect('/dashboard')


@app.route('/meal/<int:meal_id>')
def r_show_meal(meal_id):
    meal_data = Meal.get_meal({'id': meal_id})

    return render_template('one_meal.html', meal = meal_data[0], ingredients = meal_data[1])