from flask import Flask, render_template

app = Flask("flaskProject")


@app.route("/")
def hello_world():
    return render_template("index.html"), 200


@app.route("/about")
def about():
    return render_template("about/index.html"), 200


@app.route("/profile/<name>/<email>")
def profile(name, email):
    return render_template("profile/index.html",
        name=name,
        email=email), 200


app.run()
