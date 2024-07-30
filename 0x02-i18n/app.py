#!/usr/bin/env python3
import pytz
from datetime import datetime
from flask import Flask, request, g, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr'])

@babel.timezoneselector
def get_timezone():
    user_timezone = request.args.get('timezone', default='UTC')
    try:
        return pytz.timezone(user_timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return pytz.timezone('UTC')

@app.route('/')
def index():
    tz = get_timezone()
    now = datetime.now(tz)
    current_time = now.strftime("%b %d, %Y, %H:%M:%S %p")
    return render_template('index.html', current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)
