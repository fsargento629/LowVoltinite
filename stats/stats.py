import pandas as pd
import numpy as numpy
from datetime import datetime

#definições

FICHEIRO_DATA = "ana/dados2.csv"


#start

data = pd.read_csv(FICHEIRO_DATA)
'''data['diferenca'] = 0
for index,row in data.iterrows():
    try:
        row['diferenca'] = row['quantidade'] - data.at[index-1,"quantidade"]
        

    except :
        pass
       
   ''' 
data["dif"] = 0.0
data["ano"] = 0
data["mes"] = 0
data["dia"] = 0
print(data)

def preco_jan(data):
    taxa = 0.22
    preco = 0
    #simples

    for i in range (data.shape[0]):
        preco = preco + taxa * data.at[i,"dif"]
    return preco



    




'''for index,row in data.iterrows():
   # print(data.at[index,"data"])
   print(row["quantidade"])'''

for i in range (data.shape[0]-2):
    dif = float(data.at[i+1,"quantidade"])-float(data.at[i,"quantidade"])
    data.at[i,"dif"] = dif

for i in range(data.shape[0]):
    string = data.at[i,"data"]
    string_refinada = datetime.strptime(string,'%Y-%m-%d')
    data.at[i,"dia"] = string_refinada.day
    data.at[i,"mes"] = string_refinada.month
    data.at[i,"ano"] = string_refinada.year


print(preco_jan(data))

#print(data)



#create new data frame with: data hora aumento em kwh aumento em $$ e em CO2
