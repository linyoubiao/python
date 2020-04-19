"""
Github and Flask example
by LinYoUBiAo
2020-04-19
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)

