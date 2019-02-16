import pandas as pd
import numpy as np
from datetime import datetime
import calendar

#vai buscar os dados ao ficheiro csv
dados = pd.read_csv('dados2.csv')
dados = dados.loc[:, ~dados.columns.str.contains('^Unnamed')] #remove as colunas a mais
#print(dados.head())
#print(dados.index)
#print(dados.columns)
#print(dados['data'].head())
#print(dados['hora'].head())
#print(dados['quantidade'].head())
#print(dados[30:37])
#print(dados.iloc[3])


#TRATAMENTO DOS DADOS POR DIA
#cria um DataFrame para os vários dias
dados_dia = pd.DataFrame(columns=['data', 'quantidade'])

#preenche o dados_dia
for i in range(dados.shape[0]):
    if(int(dados['hora'][i])==23):
        add = pd.DataFrame([[dados['data'][i],dados['quantidade'][i]]], columns=['data', 'quantidade'])
        dados_dia = dados_dia.append(add, ignore_index=True)
if(int(dados['hora'][dados.shape[0]-1])!=23):
    add = pd.DataFrame([[dados['data'][i],dados['quantidade'][i]]], columns=['data', 'quantidade'])
    dados_dia = dados_dia.append(add, ignore_index=True)

#DataFrame de apoio
dados_dia2 = dados_dia.copy()

#passa a quantidade absoluta para a quantidade por dia
for i in range(1, dados_dia.shape[0]):
    dados_dia['quantidade'][i] = dados_dia2['quantidade'][i] - dados_dia2['quantidade'][i-1]

print(dados_dia)
#prepara os dados para o gráfico desta semana
semana = {'Segunda': 0, 'Terça': 0, 'Quarta' : 0, 'Quinta' : 0, 'Sexta' : 0, 'Sábado' : 0, 'Domingo' : 0 }

for i in range(dados_dia.shape[0]):
    dados_dia['data'][i] = datetime.strptime(dados_dia['data'][i], '%Y-%m-%d').date()
    #print(calendar.day_name[dados_dia['data'][i].weekday()])

if(dados_dia.shape[0]<7):
    for i in range(dados_dia.shape[0]):
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Monday'):
            semana['Segunda'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Tuesday'):
            semana['Terça'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Wednesday'):
            semana['Quarta'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Thursday'):
            semana['Quinta'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Friday'):
            semana['Sexta'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Saturday'):
            semana['Sábado'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Sunday'):
            semana['Domingo'] = round(dados_dia['quantidade'][i],2)
else:
    for i in range(dados_dia.shape[0]-7, dados_dia.shape[0]):
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Monday'):
            semana['Segunda'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Tuesday'):
            semana['Terça'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Wednesday'):
            semana['Quarta'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Thursday'):
            semana['Quinta'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Friday'):
            semana['Sexta'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Saturday'):
            semana['Sábado'] = round(dados_dia['quantidade'][i],2)
        if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Sunday'):
            semana['Domingo'] = round(dados_dia['quantidade'][i],2)

print(semana)
