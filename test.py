

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
    print(primeiro_digito)
    print(segundo_digito)

    if primeiro_digito == 10:
        primeiro_digito = 0
    if segundo_digito == 10:
        segundo_digito = 0



    if primeiro_digito == cpf_separado[9] and segundo_digito == cpf_separado[10]:
        return True
    else:
        return False

print(validar_cpf(input('escreva seu cpf: ')))
