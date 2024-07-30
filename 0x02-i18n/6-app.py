#!/usr/bin/env python3
"""
Initialisation d'une application Flask avec Babel
pour la localisation des textes.
Ce script gère également la simulation d'une connexion utilisateur
et ajuste la localisation
selon les paramètres d'URL, les préférences de l'utilisateur,
ou les en-têtes de la requête.
"""

from flask import Flask, request, g, redirect, url_for, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    # Assuming 'kg' is not a valid locale
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config['BABEL_DEFAULT_LOCALE'] = 'en'


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
    # Check URL parameters first
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Then check user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Then use request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
