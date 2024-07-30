#!/usr/bin/env python3
"""
Initialisation application Flask avec Babel pourlocalisation des textes.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
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
    Affiche la page d'accueil avec localisation.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
