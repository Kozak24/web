from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    news = [
        {
            'author': {'username': 'Admin'},
            'article': 'Path of the Ninja V0.005',
            'body': 'Improved AI & battle system (added defense and DoT effect)'
        },
        {
            'author': {'username': 'Kozak'},
            'article': 'Path of the Ninja V0.005 Camera improvement',
            'body': 'Camera  configured for all screen resolutions'
        }
    ]
    user = {'username': "Kozak"}
    return render_template('index.html', title='Home page', user=user, news=news)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if (form.validate_on_submit()):
        flash('Login requested for user {}, remember_me {}'.format(
            form.username.data, form.remember_me.data ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
