from datetime import datetime

data_atual =  datetime.now() #exibe a data/hora atual
print(data_atual)

import datetime
td = datetime.timedelta(hours=-5)
print(td)
print(data_atual+td)