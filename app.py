

def validar_cpf(inputCpf):   
    cpf_pontuado = inputCpf
    cpf = ''

    def verificar_numero(numero:str):
        if numero.isnumeric():
            return True
        else:
            return False

    for digito in cpf_pontuado:
        if verificar_numero(digito):
            cpf += digito

    cpf_separado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



    for numero in range(0, len(cpf)):
        cpf_separado[numero] = cpf[numero]
        cpf_separado[numero] = int(cpf_separado[numero])

    primeiro_digito = 0
    segundo_digito = 0

    for numero in range(0, len(cpf) - 2):
        primeiro_digito += cpf_separado[numero] * (10 - numero)
        
    for numero in range(0, len(cpf) - 1):
        segundo_digito += cpf_separado[numero] * (11 - numero)



    primeiro_digito *= 10
    primeiro_digito %= 11
    segundo_digito *= 10
    segundo_digito %= 11

    if primeiro_digito == 10:
        primeiro_digito = 0
    if segundo_digito == 10:
        segundo_digito = 0



    if primeiro_digito == cpf_separado[9] and segundo_digito == cpf_separado[10]:
        return True
    else:
        return False
        

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/', methods=["POST"])
def colect_cpf():
    cpf = request.form.get('CPF')
    if validar_cpf(cpf):
        return '<h1>Este CPF é válido</h1> <a href="/"><button>voltar</button></a>'
    else:
        return '<h1>Este CPF não é válido</h1> <a href="/"><button>voltar</button></a>'

if __name__ == "__main__":
    app.run(debug=True)
