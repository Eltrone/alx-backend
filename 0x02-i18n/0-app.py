#!/usr/bin/env python3
"""
Ce module contient une application Flask basique.
Il définit une route unique qui affiche un message d'accueil.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """ Affiche la page d'accueil avec un titre et un message. """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run()
