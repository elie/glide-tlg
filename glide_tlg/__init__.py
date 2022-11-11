from os import path

version = "1.5.0"


def setup(app):
    app.add_html_theme(
        'revealjs-tlg',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "revealjs-tlg")))
    app.add_html_theme(
        'handouts-tlg',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "handouts-tlg")))
