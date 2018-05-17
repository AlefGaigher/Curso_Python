num = int(input("Digite a sua idade: "))

if num < 14:
    tipo="Criança"
elif num >= 14 and num <26:
    tipo="Jovem"
elif num >= 26 and num <65:
    tipo="Adulto"
else:
    tipo="3a Idade"

print('O número {} é {}'.format(num, tipo))
