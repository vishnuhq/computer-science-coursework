from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/<username>")
def hello_name(username=None):
    return render_template("index.html", name=username)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
