from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("console here")
    return "<p>Hello, World!</p>"


@app.route("/double/<x>")
def double(x):
    y = int(x)
    print("doubler")
    return "<p>x</p>" + str(2 * y)


if __name__ == '__main__':
    app.run('0.0.0.0', 8085)