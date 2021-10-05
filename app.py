from flask import Flask, render_template

app = Flask("flaskProject")

@app.route("/")
def hello_world():
    return render_template("index.html"), 200


@app.route("/about")
def about():
    return render_template("about/index.html"), 200


app.run()
