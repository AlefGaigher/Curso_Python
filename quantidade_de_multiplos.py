multiplos_2 = 0
multiplos_3 = 0
multiplos_5 = 0
multiplos_7 = 0
multiplos_11 = 0

sequencia = range (2, 1001)
print(list (sequencia))
for numero in sequencia:
    if numero % 2 == 0:
        #multiplos_2 = multiplos_2+1
        multiplos_2 += 1
    if numero % 3 == 0:
        multiplos_3 += 1
    if numero % 5 == 0:
        multiplos_5 += 1
    if numero % 7 == 0:
        multiplos_7 += 1
    if numero % 11 == 0:
        multiplos_11 += 1

print("Existem {} multiplos de 2" .format(multiplos_2))
print("Existem {} multiplos de 3" .format(multiplos_3))
print("Existem {} multiplos de 5" .format(multiplos_5))
print("Existem {} multiplos de 7" .format(multiplos_7))
print("Existem {} multiplos de 11" .format(multiplos_11))



