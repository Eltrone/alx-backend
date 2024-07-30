#!/usr/bin/env python3
"""
Initialisation application Flask avec Babel pourlocalisation des textes.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
