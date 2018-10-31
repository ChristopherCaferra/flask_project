from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World! :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/Converter')
@app.route('/Converter/<celsius>')
def converter(celsius=""):
    fahrenheit = float(celsius) * 9 / 5.0 + 32
    return "{} degrees celsius converts to {:.2f} degrees fahrenheit".format(celsius, fahrenheit)


if __name__ == '__main__':
    app.run()
