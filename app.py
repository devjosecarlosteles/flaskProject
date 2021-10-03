from flask import Flask, render_template

app = Flask("flaskProject")

@app.route("/")
def hello_world():
    return "Olá Mundo! Esse é meu primeiro projeto flask!", 200

app.run()