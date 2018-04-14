sequencia = range (1, 200)

for numero in sequencia:
    #if numero % 3 == 0:
    #    divisivel_3 = True
    #else:
    #    divisivel_3 = False
    divisivel_3 = numero % 3 == 0

    #if nuemro %5 == 0:
    #    divisivel_5 = True
    #else:
    #    divisivel_5 = False
    divisivel_5 = numero % 5 == 0

    if divisivel_3 and divisivel_5:
        print('FizzBuzz')
    elif divisivel_3:
        print('Fizz')
    elif divisivel_5:
        print("Buzz")
    else:
        print(numero)