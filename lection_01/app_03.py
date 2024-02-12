from flask import Flask

app = Flask(__name__)

@app.route('/John/')
@app.route('/john')
@app.route('/Джон/')
def john():
    return 'Привет, Джони!'


if __name__ == '__main__':
    app.run(debug=True)