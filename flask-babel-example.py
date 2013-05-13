from flask import Flask, request
from flaskext.babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'es'])


@app.route('/')
def hello_world():
    return gettext('Hello World!')


if __name__ == '__main__':
    app.run()
