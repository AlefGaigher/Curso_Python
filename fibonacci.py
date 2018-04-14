n = int(input('Informe um Número: '))

fibonacci = [0 , 1]

numero1 = 0
numero2 = 1

for x in range (1, n +1):
    numero3 = numero1 + numero2
    fibonacci.append(numero3)
    numero1 = numero2
    numero2 = numero3

print(len(fibonacci))
print(fibonacci)
print(fibonacci[n-1])

    