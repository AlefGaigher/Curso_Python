lista = [1,1,2,3,4,3,2]
lista_auxiliar = []

for item in lista:
    if item not in lista_auxiliar:
        lista_auxiliar.append(item)

print(lista_auxiliar)
print(set(lista))
    