from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'You went somewhere you should not have'

@app.route('/herro')
def add():
    return render_template('index.html')

    
@app.route('/add_food', methods=['POST'])
def add_food():
    if request.method == 'POST':
        for key in request.form:
            print(request.form[key])
        return 'Hello world'
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)