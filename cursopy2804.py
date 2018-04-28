lista_de_listas=[[1,2,3],[4,5,6],[7,8,9]]
lista_final = []
 # for elemento in lista_de_listas:
 #     for elemento2 in elemento:
 #         #print (elemento2) #para aperecer um embaixo do outro
 #         lista_final.append(elemento2)
 # print (lista_final)
lista_final = [elemento2 for elemento in lista_de_listas for elemento2 in elemento]
print (lista_final)