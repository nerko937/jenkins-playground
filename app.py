from flask import Flask

app = Flask(__name__)


def get_message():
    return 'Hello World!'


@app.route('/')
def hello():
    return get_message()

