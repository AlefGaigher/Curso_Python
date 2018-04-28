valores = input('digite uma lista de valores: ')
lista_de_valores = valores.split(',')
print(lista_de_valores)
soma=0
for indice, valor in enumerate (lista_de_valores):
    lista_de_valores[indice] = int(valor)
    soma+= int(valor)
print('valor: {}'.format(soma))
lista_de_valores.sort()
if len(lista_de_valores)>=2:
    print('Segundo maior elemento: {}'.format(lista_de_valores[-2]))
else:
    print('Apenas um Elemento')