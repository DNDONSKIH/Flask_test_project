from flask import Flask


app = Flask(__name__)


@app.route('/<a>/<b>')
def index(a, b):
    return f'{a}/{b}Hello, world!!!1'


if __name__ == '__main__':
    app.run()
