import random

while True:
    numero_sorteado = random.randint ( 1 , 10 )

    print ( numero_sorteado )

    tentativas = 0
    numero_escolhido = 0

    while numero_escolhido != numero_sorteado:
        tentativas += 1
        numero_escolhido = int ( input ( "Escolha um Número: " ) )

print ( "Ele acertou em {} tentativa(s)".format ( tentativas ) )
