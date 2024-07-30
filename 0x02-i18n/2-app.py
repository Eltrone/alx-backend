#!/usr/bin/env python3
"""
Initialisation d'une application Flask avec Babel pour
la sélection de langue basée sur la requête de l'utilisateur.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)


class Config:
    """
    Configuration de Babel avec les langues et paramètres par défaut.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Sélectionne la locale adaptée à partir de la requête HTTP.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Affiche la page d'accueil.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
