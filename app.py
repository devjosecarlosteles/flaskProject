from flask import Flask, render_template

app = Flask("flaskProject")

@app.route("/")
def hello_world():
    return render_template("index.html", name="José Carlos Teles", age=17), 200

app.run()