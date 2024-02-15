from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Привет, незнакомец!'

@app.route('/name/')
def aub():
    return 'Привет, Name!'

@app.route('/Ваня/')
def ivan():
    return 'Привет, Ваня!'



if __name__ == '__main__':
    app.run(debug=True)