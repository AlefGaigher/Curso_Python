lista = range(100)
# num2  =  {numero for  numero  in  range(100)  if  numero  %  2  ==  0}
# num3  =  {numero for  numero  in  range(100)  if  numero  %  3  ==  0}
# num5  =  {numero for  numero  in  range(100)  if  numero  %  5  ==  0}
# num7  =  {numero for  numero  in  range(100)  if  numero  %  7  ==  0}
# print('Multiplo de 2: {}'.format(num2))
# print('Multiplo de 3: {}'.format(num3))
# print('Multiplo de 5: {}'.format(num5))
# print('Multiplo de 7: {}'.format(num7))
dic = {
    2: [],
    3: [],
    5: [],
    7: [],
    'nenhum': []
}

# for numero in lista:
#     if numero %2 == 0:
#         dic[2].append(numero)
#     if numero %3 == 0:
#         dic[3].append(numero)
#     if numero %5 == 0:
#         dic[5].append(numero)
#     if numero %7 == 0:
#         dic[7].append(numero)

for numero in lista
    divisivel_2 = numero % 2 == 0
    divisivel_3 = numero % 2 == 0
    divisivel_5 = numero % 2 == 0
    divisivel_7 = numero % 2 == 0

    if divisivel_2:
        dic[2].append(numero)
    if divisivel_2:
        dic[3].append(numero)
    if divisivel_2:
        dic[5].append(numero)
    if divisivel_2:
        dic[7].append(numero)


print(dic)