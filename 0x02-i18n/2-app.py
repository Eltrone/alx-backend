#!/usr/bin/env python3
"""
Ce module configure Flask et Babel pour une application multilingue avancée,
sélectionnant la langue basée sur les préférences de l'utilisateur.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, localeselector

app = Flask(__name__)


class Config:
    """ Configuration de base pour l'application Flask utilisant Babel. """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Sélect best langue disponible en fonction de la requête """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Affiche la page d'accueil. """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
