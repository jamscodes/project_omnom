from flask_app import app
from flask import render_template, request, redirect


@app.route('/add-food')
def r_add_food():
    return render_template('add_food.html')


@app.route('/add_food', methods=['POST'])
def f_add_food():
    for field in request.form:
        print(field)
    return redirect('/')