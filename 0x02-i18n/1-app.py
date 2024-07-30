#!/usr/bin/env python3
"""
Ce module configure Flask et Babel pour une application multilingue de base.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Configuration de base pour l'application Flask utilisant Babel. """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ Affiche la page d'accueil. """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
