
frase= input('Digite uma frase: ')
frase= frase.lower().replace (' ','')
lista_invertida = [caracter for caracter in frase]
lista_invertida.reverse()
frase_invertida = ''.join(lista_invertida)
#frase = frase.replace('','')
#print (frase)
#print(frase_invertida)
#luz azul

if frase == frase_invertida:
    print ('É um Palindromo!')
else:
    print ('Não é um Palindromo!')