from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from travel.form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1c1331abccfb1bb9d8294722675c2907'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home", page='home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        
            return redirect(url_for('welcome'))  # Redirect to welcome page
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/welcomepage")
def welcome():
    destinations = [
        {'name': 'Paris', 'image': 'paris.avif'},
        {'name': 'New York', 'image': 'newyork.webp'},
        {'name': 'Tokyo', 'image': 'tokyo.avif'},
        {'name': 'London', 'image': 'london.avif'},
    ]
    return render_template('welcomepage.html', title='Welcome', destinations=destinations)

if __name__ == '__main__':
    app.run(debug=True)