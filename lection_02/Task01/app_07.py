from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the app_07 page"

@app.route('/submit', methods=['Get', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form2.html')


if __name__ == '__main__':
    app.run(debug=True)