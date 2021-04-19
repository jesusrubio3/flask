from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")


app.run("0.0.0.0",8000,debug=True)

