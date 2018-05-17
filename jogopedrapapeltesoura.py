while 'sair':
    option1= str(input("Digite a sua escolha Jogador 1 (Pedra, Papel ou Tesoura): "))
    option2= str(input("Digite a sua escolha Jogador 2 (Pedra, Papel ou Tesoura): "))

    if option1 == option2:
        print('Deu Empate!')
    elif option1 == 'Pedra' and option2 == 'Tesoura' or option1 == 'Papel' and option2 == 'Pedra' or option1 == 'Tesoura' and option2 == 'Papel':
        print('Jogador 1 Ganhou')
    elif option2 == 'Pedra' and option1 == 'Tesoura' or option2 == 'Papel' and option1 == 'Pedra' or option2 == 'Tesoura' and option1 == 'Papel':
        print('Jogador 2 Ganhou')



