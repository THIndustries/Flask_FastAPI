from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return 'Введи путь в адресной строке'

@app.route('/<path:file>/')
def get_file(file):
    print(file)
    #return f'Файл находится в {file}'
    return f'Файл находится в {escape(file)}'


if __name__ == '__main__':
    app.run(debug=True, port=5004)