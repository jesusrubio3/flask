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
    return render_template("potencia.html",base=base,exponente=exponente,resultado=resultado)

@app.route('/cuenta/<palabra>/<letra>')
def cuentaletras(palabra,letra):
    veces=palabra.count(letra)
    if len(letra)>1:
         abort(404)
    
    return render_template("cuentaletras.html",palabra=palabra,letra=letra,veces=veces)

@app.route('/libros/<codigo>')
def libros(codigo):
    codigolibro=int(codigo) 
    fichero=etree.parse("libros.xml")
    autor=fichero.xpath("/biblioteca/libro[codigo=%d]/autor/text()"%codigolibro)
    titulo=fichero.xpath("/biblioteca/libro[codigo=%d]/titulo/text()"%codigolibro)
    if len(autor)==0:
        abort(404)
    for i in autor:
        i=i
    autor=i
    for j in titulo:
        j=j
    titulo=j
    return render_template("libros.html",autor=autor,titulo=titulo)

app.run("0.0.0.0",8000,debug=True)

