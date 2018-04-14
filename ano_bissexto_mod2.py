def is_leap_year(ano):
    if ano %4 == 0:
        if ano %100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

    return (ano % 4 == 0) and\
           (((ano % 100 == 0) and (ano % 400 == 0)) or (ano!=0))
while True:
    ano = int (input('Digite um ano: '))
    print(is_leap_year(ano))