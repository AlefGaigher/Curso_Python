print('Este é meu primeiro modulo\n')

from db.conexoes import conectar_com_oracle, conectar_com_mysql  #".pasta" pra definir diretorios , e "," para acrescentar ouytras importações
conectar_com_oracle()
conectar_com_mysql()

texto =""" 
Nunca pode ser aspas duplas, 
sempre aspas triplas para definição 
de streams multi linhas
"""

