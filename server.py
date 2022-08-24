from flask import Flask, render_template, request, redirect
from db import foods

app = Flask(__name__)

@app.route('/add-food')
def r_add_food():
    return render_template('add_food.html')


@app.route('/add_food', methods=['POST'])
def f_add_food():
    for field in request.form:
        print(field)
    return redirect('/')


@app.route('/add-meal')
def r_add_meal():
    all_foods = foods
    return render_template('add_meal.html', food_items = all_foods)


@app.route('/add_meal', methods=['POST'])
def f_add_meal():
    for field in request.form:
        print(field)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)