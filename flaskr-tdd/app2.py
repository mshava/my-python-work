from flask import flask
from flask import render_template
app = flask(__name__)
@app.route("/")
def main():
	return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)