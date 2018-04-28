frase = input ('Digite uma Frase: ')
lista = frase.split(' ')
#minha frase => ['Minha', 'frase"]
lista.reverse()
#minha frase => ['Minha', 'frase'] => ['frase', 'minha']
frase=' '.join(lista)
print('Frase com as palavras invertidas: {}'.format(frase))