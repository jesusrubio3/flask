from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/potencia/<base>/<exponente>')
def potencia(base,exponente):
    try:
        base=int(base)
        exponente=int(exponente)
        resultado=base**exponente
    except:
        abort(404)
    return render_template("potencia.html",base=base,exponente=exponente,result$



app.run("0.0.0.0",8000,debug=True)

