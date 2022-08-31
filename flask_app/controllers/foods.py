from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.food import Food


@app.route('/food/add-food')
def r_add_food():
    return render_template('add_food.html')


@app.route('/food/add_food', methods=['POST'])
def f_add_food():
    data = {
        'name': request.form.get('food_name'),
        'calories': request.form.get('food_calories'),
        'serving_size': request.form.get('food_serving_size'),
        'measurement_type': request.form.get('food_measurement_type')
    }

    new_food_id = Food.add_food(data)

    return redirect(f'/food/{new_food_id}')


@app.route('/food/<int:food_id>')
def r_one_food(food_id):
    data = {
        'id': food_id
    }

    food = Food.get_food(data)

    return render_template('one_food.html', food = food)


@app.route('/food/update/<int:food_id>')
def r_update_food(food_id):
    data = {
        'id': food_id
    }

    food = Food.get_food(data)

    return render_template('update_food.html', food = food)


@app.route('/food/update_food', methods = ['POST'])
def f_update_food():
    data = {
        'id': request.form.get('food_id'),
        'name': request.form.get('food_name'),
        'calories': request.form.get('food_calories'),
        'serving_size': request.form.get('food_serving_size'),
        'measurement_type': request.form.get('food_measurement_type'),
    }

    Food.update_food(data)

    return redirect(f'/food/{data["id"]}')