from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Проект с наследованием шаблонов'

@app.route('/main/')
def main():
    context = {'title': 'Main'}
    return render_template('main.html', **context)

@app.route('/data/')
def data():
    context = {'title': 'Data'}
    return render_template('data.html', **context)


if __name__ == '__main__':
    app.run(debug=True, port=5002)