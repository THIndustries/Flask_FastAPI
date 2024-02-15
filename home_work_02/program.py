from flask import Flask, request, render_template, url_for, make_response, redirect, flash

app = Flask(__name__)

app.secret_key = 'и так сойдёт'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration/', methods = ['GET', 'POST'])
def regisеt():
    if request.method == "POST":
        #считываю данные из формы
        name = request.form['name']
        email = request.form['email']
        #настраиваю cookie с данными пользователя
        response = make_response(render_template('hello.html', name=name))
        response.set_cookie('user_data',f'{name}, {email}')

        flash('Cookie успешно созданы!', 'sucess')

        return response

    return render_template('form.html')

@app.route('/logout/')
def logout():
    #Удаление cookie с данными пользователя
    resource = make_response(redirect(url_for('index')))
    resource.delete_cookie('user_data')

    flash('Cookie успешно удалены!', 'success')

    return resource

if __name__ == '__main__':
    app.run(debug=True)