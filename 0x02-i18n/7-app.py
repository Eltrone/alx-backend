#!/usr/bin/env python3
"""
Initialisation d'une application Flask avec Babel
pour la localisation des textes
et la gestion des fuseaux horaires.
"""

from flask import Flask, request, g, render_template
from flask_babel import Babel, gettext
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)

# Configuration par défaut pour la localisation et le fuseau horaire
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale and locale in ['en', 'fr']:
        return locale
    if g.user and g.user['locale'] in ['en', 'fr']:
        return g.user['locale']
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    tz_name = request.args.get('timezone')
    if tz_name:
        try:
            pytz.timezone(tz_name)
            return tz_name
        except UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass
    return 'UTC'


# Adding functions to Jinja global environment
app.jinja_env.globals['get_locale'] = get_locale
app.jinja_env.globals['get_timezone'] = get_timezone


@app.route('/')
def index():
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(debug=True)
