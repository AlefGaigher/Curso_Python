while True:
    linhas = int(input('Digite a quantidade de Linhas: '))
    maior_linha = (linhas *2)-1
    quantidade = 1
    for x in range (1, linhas +1):
        texto = '#' * quantidade

        print(texto.center(maior_linha))
        quantidade += 2

