from flask import Flask

app = Flask(__name__)


@app.get('/')
def hello_world():
    return "Hello World!"


@app.get('/json')
def json():
    return {"key": "value", "another": "value2"}


if __name__ == '__main__':
    app.run(debug=True)
