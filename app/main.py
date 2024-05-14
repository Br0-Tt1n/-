from flask import Flask, render_template, redirect, url_for, request

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

admin_rule = False
login_user = False


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/price')
def price():
    return render_template('price.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/profile')
def profile():
    return render_template('profile.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login_email = request.form['login_email']
        login_password = request.form['login_password']
        global admin_rule
        global login_user
        if login_email == "admin" and login_password == "admin":
            admin_rule = True
            print(admin_rule)
        login_user = True
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        # это нам могло понадобитсья будь у нас база данных
        # in1 = request.form.get('in1')
        # in2 = request.form.get('in2')
        # in4 = request.form.get('in4')
        # in5 = request.form.get('in5')
        # in6 = str(request.form.get('in6'))
        # in7 = request.form.get('in7')
        # in8 = request.form.get('in8')
        return redirect('index')
    return render_template('registration.html')


@app.route('/work')
def our_work():
    return render_template('our_work/ourWork.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/Balkon')
def work_balkon():
    return render_template('our_work/Balkon.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/BesedkiPeregorodki')
def work_BesedkiPeregorodki():
    return render_template('our_work/BesedkiPeregorodki.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/Doma')
def work_doma():
    return render_template('our_work/Doma.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/Dveri')
def work_dveri():
    return render_template('our_work/Dveri.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/Okna')
def work_okna():
    return render_template('our_work/Okna.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/Proizvodstvo')
def work_proizvodstvo():
    return render_template('our_work/Proizvodstvo.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/contact')
def contact():
    return render_template('/contact.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global login_user
    global admin_rule
    login_user = False
    admin_rule = False
    return render_template('index.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/order')
def order():
    return render_template('order.html', admin_rule=admin_rule, login_user=login_user)


@app.route('/buy')
def buy():
    return render_template('buy.html', admin_rule=admin_rule, login_user=login_user)


if __name__ == '__main__':
    # установить значение хоста, чтобы вывести в сеть
    # (host='0.0.0.0')
    app.run(debug=True)
