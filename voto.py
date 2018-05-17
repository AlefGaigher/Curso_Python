ano_nascimento = -1
while ano_nascimento != 0:
    ano_nascimento= int(input("informe seu a ano de nascimento: "))
    ano_votacao = ano_nascimento+16
    if ano_nascimento + 16 >= 1988:
        print("Você podia votar no ano {}".format(ano_votacao))
    else:
        ano_votacao = ano_nascimento+17
        if ano_votacao >= 1988:
            print("Você Podia votar no ano {}".format(ano_votacao))
        else:
            ano_votacao = ano_nascimento + 18
            print("Você podia votar no ano {}".format(ano_votacao))