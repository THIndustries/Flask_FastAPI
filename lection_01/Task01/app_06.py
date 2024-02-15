from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Project main"

@app.route('/if/')
def show_if():
    context = {
        'title': 'Условые операторы и ветвления',
        'user': 'Неофит',
        'number': 1,
    }

    return render_template('show_if.html', **context)



if __name__ == '__main__':
    app.run(debug=True)