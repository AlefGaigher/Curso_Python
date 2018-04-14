def fatorial (numero):
    lista_numeros= range(1, numero +1)
    print(list(lista_numeros))

    fatorial =1
    for x in lista_numeros:
        fatorial = fatorial * x

    return fatorial

def fatorial_com_recursao(numero):
    if numero ==1:
        return 1
    return numero+ fatorial_com_recursao (numero -1)

while True:
    numero = int (input('informe um número: '))
    print (fatorial(numero))
    print(fatorial_com_recursao(numero))