from flask import Flask, render_template, flash, redirect, url_for, request

from app.forms import LoginForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

admin_rule = False


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/price')
def price():
    return render_template('price.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        login_email = request.form.get('login_email')
        login_password = request.form.get('login_password')
        global admin_rule
        if login_email == "admin" and login_password == "admin":
            admin_rule = True
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        in1 = request.form.get('in1')
        in2 = request.form.get('in2')
        in4 = request.form.get('in4')
        in5 = request.form.get('in5')
        in6 = str(request.form.get('in6'))
        in7 = request.form.get('in7')
        in8 = request.form.get('in8')
        return redirect('index')
    return render_template('registration.html')


@app.route('/work')
def our_work():
    return render_template('our_work/ourWork.html')


@app.route('/Balkon')
def work_balkon():
    return render_template('our_work/Balkon.html')


@app.route('/BesedkiPeregorodki')
def work_BesedkiPeregorodki():
    return render_template('our_work/BesedkiPeregorodki.html')


@app.route('/Doma')
def work_doma():
    return render_template('our_work/Doma.html')


@app.route('/Dveri')
def work_dveri():
    return render_template('our_work/Dveri.html')


@app.route('/Okna')
def work_okna():
    return render_template('our_work/Okna.html')


@app.route('/Proizvodstvo')
def work_proizvodstvo():
    return render_template('our_work/Proizvodstvo.html')


@app.route('/contact')
def contact():
    return render_template('/contact.html')


if __name__ == '__main__':
    # установить значение хоста, чтобы вывести в сеть
    # (host='0.0.0.0')
    app.run(debug=True)
