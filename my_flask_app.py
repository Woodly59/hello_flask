from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!我不知道加啥，我也加一句话吧</p>"


if __name__ == '__main__':
    app.run()