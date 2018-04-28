A = [1,2,3,4,5,6,7,8,9,10]
B = [1,1,2,3,5,8,13,21,34,55]
#Imprimir Itens Unicos de A e B
print('Quantidade de elementos únicos em A: {}'.format(len(A)))
set_A = set(A)
set_B = set(B)
print('Quantidade de elementos únicos em B: {}'.format(len(set_B)))
print((A[:]))
#Criar Lista C com itens unicos de A e B
C = A[:]
for item in B:
    if item not in C:
        C.append(item)
print('C => {}'.format(C))
#Liste os Elementos em comum em  cada Lista
print('Itens Comuns: {}'.format(list(set_A.intersection(set_B))))
#Liste os elementos de A que não estão em B
print('Diferenças em A: {}'.format(list(set_A.difference(set_B))))
#Liste os elementos de B que não estão em A
print('Diferenças em B: {}'.format(list(set_B.difference(set_A))))