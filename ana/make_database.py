import pandas as pd
from datetime import datetime, timedelta
import random

dados= pd.DataFrame(columns=['data', 'hora', 'quantidade'])
a = datetime(2019,1,1)
b = a + timedelta(days=1)

for i in range(31):
    b = a + timedelta(days=i)
    s = str(b.year) + '-' + str(b.month) + '-' + str(b.day)
    for i in range(24):
        add = pd.DataFrame([[0,0,0]], columns=['data', 'hora', 'quantidade'])
        add['hora'] = i
        add['data'] = s
        dados = dados.append(add, ignore_index=True)

for i in range(dados.shape[0]-1):
    dados['quantidade'][i+1] = dados['quantidade'][i] + random.uniform(0,3.2)

print(dados)
dados.to_csv("dados7.csv")
