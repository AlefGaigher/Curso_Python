pessoa = {}
pessoa['nome'] = 'Alef'
pessoa['ano_nascimento'] = 1993
pessoa['premios'] = []
pessoa['filiacao'] = {'pai':'Nome do Pai ', 'mae':'Nome da Mãe'}
#pessoa['premios'].append('Prêmio 1')
#print(pessoa['qualquer elemento que vc queira q apareça aqui'])
print(pessoa)
#print('Nome do pai: {}'.format(pessoa['filiacao']['valor: pai ou mae']))
print('Nome do pai: {}'.format(pessoa['filiacao']['pai']))
#outras propriedades
print('Len => {}'.format(len(pessoa)))
print('Keys => {}'.format(pessoa.keys()))
print('Values => {}'.format(pessoa.values()))
print('Items => {}'.format(pessoa.items()))
#usando for
for chave in pessoa.keys():
    print('Chave: {}'.format(chave))
for valor in pessoa.values():
    print('Valor: {}'.format(valor))
for chave, valor in pessoa.items():
    print('Chave: {} | Valor: {}'.format(chave,valor))
#para alterar valores ou adicionar
pessoa.update({'nome': 'Pedro', 'cidade': 'Vila Velha'})
pessoa.update({})
print(pessoa)
#para deletar valores
del pessoa['filiacao']
print(pessoa)

