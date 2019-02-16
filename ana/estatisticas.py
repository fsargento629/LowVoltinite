from csv import reader
import calendar
import pygal
import pandas as pd
import numpy as np
import numpy as np
from datetime import datetime
import os


def ler_dados():
    #vai buscar os dados ao ficheiro csv
    dados = pd.read_csv('dados2.csv')
    dados = dados.loc[:, ~dados.columns.str.contains('^Unnamed')] #remove as colunas a mais
    return dados

def estatisticas_semana(dados):
    #TRATAMENTO DOS DADOS POR DIA
    #cria um DataFrame para os varios dias
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

    #prepara os dados para o grafico desta semana
    semana = {'Segunda': 0, 'Terça': 0, 'Quarta' : 0, 'Quinta' : 0, 'Sexta' : 0, 'Sabado' : 0, 'Domingo' : 0 }

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
                semana['Sabado'] = round(dados_dia['quantidade'][i],2)
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
                semana['Sabado'] = round(dados_dia['quantidade'][i],2)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Sunday'):
                semana['Domingo'] = round(dados_dia['quantidade'][i],2)


    #GRaFICO DA SEMANA
    week_graph=pygal.Bar(width=1000)
    week_graph.title = "Consumo na semana"

    week_graph.add("Segunda", semana['Segunda'])
    week_graph.add("Terça", semana['Terça'])
    week_graph.add("Quarta", semana['Quarta'])
    week_graph.add("Quinta", semana['Quinta'])
    week_graph.add("Sexta", semana['Sexta'])
    week_graph.add("Sabado", semana['Sabado'])
    week_graph.add("Domingo", semana['Domingo'])

    #week_graph.render_in_browser()
    week_graph.render_to_file('static/week_graph.svg')
    #os.rename("week_graph.svg", "/static/week_graph.svg")


dados = ler_dados()
estatisticas_semana(dados)
