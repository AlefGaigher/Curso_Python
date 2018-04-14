for numero in range (2, 101):
    divisores = 0

    for divisor in range (2, numero+1):
        if numero % divisor == 0:
            divisores += 1
    if divisores == 1:
        print(numero)
