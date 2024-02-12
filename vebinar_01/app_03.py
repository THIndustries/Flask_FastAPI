from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_peole():

    names = [
        {'name':'IVAN',
        'Lastname':'IVANOV',
         'age': 48},
        {'name': 'Petr',
         'Lastname': 'Sidorov',
        'age': 48}
    ]

    return render_template('index.html', names=names)


if __name__ == '__main__':
    app.run()