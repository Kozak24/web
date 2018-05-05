from flask import render_template
from app import app

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
