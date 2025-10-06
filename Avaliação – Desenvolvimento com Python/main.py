from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

## SOMA
@app.route(f"/soma/valor1=<int:n1>/valor2=<int:n2>") 
def soma(n1, n2):
        soma = n1 + n2
        return '<h1> A soma de {} e {} é :{} </h1>'.format(n1, n2, soma)

## SUBTRAÇÃO
@app.route(f"/subtrair/valor1=<int:n1>/valor2=<int:n2>")
def subtrair(n1, n2):
        sub = n1 - n2
        return '<h1> A subtração de {} e {} é :{}'.format(n1, n2, sub)

## DIVISÃO
@app.route(f"/divisao/valor1=<int:n1>/valor2=<int:n2>")
def dividir(n1, n2):
    if n2 == 0:
        return '<h1> A divisão de {} e {} é :{}'.format(n1, n2, 0)
    else:
        return '<h1> A divisão de {} e {} é :{}'.format(n1, n2, n1/n2)

## MULTIPLICAÇÃO
@app.route(f"/multiplicar/valor1=<int:n1>/valor2=<int:n2>")
def multiplicar(n1, n2):
        mult = n1 * n2
        return '<h1> A multiplicação de {} e {} é :{}'.format(n1, n2, mult)

if __name__ == "__main__":
    app.run(debug=True)