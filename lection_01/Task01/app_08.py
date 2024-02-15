from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "work with users"

@app.route('/users/')
def users():
    _users = [{'name': 'John',
               'mail': 'john@main.com',
               'phone': '+1-432-432-23-01',
               },
              {'name': 'Bob',
               'mail': 'Bob@main.com',
               'phone': '+2-132-462-13-61',
               },
              {'name': 'Alex',
               'mail': 'Alex@main.com',
               'phone': '+8-932-762-11-72',
               }, ]

    context = {'users': _users,
               'title': 'Точечная нотация'}

    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run()