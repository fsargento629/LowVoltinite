from csv import reader
import calendar
import pygal
from pygal.style import LightenStyle
import pandas as pd
import numpy as np
import numpy as np
from datetime import datetime
import os


def ler_dados():
    #vai buscar os dados ao ficheiro csv
    dados = pd.read_csv('dados3.csv')
    dados = dados.loc[:, ~dados.columns.str.contains('^Unnamed')] #remove as colunas a mais
    print(dados.tail())
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
    print(dados_dia)
    #passa a quantidade absoluta para a quantidade por dia
    for i in range(1, dados_dia.shape[0]):
        dados_dia['quantidade'][i] = dados_dia2['quantidade'][i] - dados_dia2['quantidade'][i-1]

    print(dados_dia)
    #prepara os dados para o grafico desta semana
    semana = {'Segunda': 0, 'Terca': 0, 'Quarta' : 0, 'Quinta' : 0, 'Sexta' : 0, 'Sabado' : 0, 'Domingo' : 0 }

    for i in range(dados_dia.shape[0]):
        dados_dia['data'][i] = datetime.strptime(dados_dia['data'][i], '%Y-%m-%d').date()
        #print(calendar.day_name[dados_dia['data'][i].weekday()])

    if(dados_dia.shape[0]<7):
        for i in range(dados_dia.shape[0]):
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Monday'):
                semana['Segunda'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Tuesday'):
                semana['Terca'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Wednesday'):
                semana['Quarta'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Thursday'):
                semana['Quinta'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Friday'):
                semana['Sexta'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Saturday'):
                semana['Sabado'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Sunday'):
                semana['Domingo'] = round(dados_dia['quantidade'][i],3)
    else:
        for i in reversed(range(dados_dia.shape[0]-7, dados_dia.shape[0])):
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Monday'):
                semana['Segunda'] = round(dados_dia['quantidade'][i],3)
                break
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Tuesday'):
                semana['Terca'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Wednesday'):
                semana['Quarta'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Thursday'):
                semana['Quinta'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Friday'):
                semana['Sexta'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Saturday'):
                semana['Sabado'] = round(dados_dia['quantidade'][i],3)
            if(calendar.day_name[dados_dia['data'][i].weekday()] == 'Sunday'):
                semana['Domingo'] = round(dados_dia['quantidade'][i],3)


    #GRAFICO DA SEMANA
    dark_lighten_style = LightenStyle('#336676')
    week_graph=pygal.Bar(width=1000, style=dark_lighten_style)
    week_graph.title = "Consumo da semana"

    week_graph.add("Segunda", semana['Segunda'])
    week_graph.add("Terca", semana['Terca'])
    week_graph.add("Quarta", semana['Quarta'])
    week_graph.add("Quinta", semana['Quinta'])
    week_graph.add("Sexta", semana['Sexta'])
    week_graph.add("Sabado", semana['Sabado'])
    week_graph.add("Domingo", semana['Domingo'])

    #week_graph.render_in_browser()
    week_graph.render_to_file('static/week_graph.svg')

def estatisticas_dia(dados):
    dia = [0.0]*24

    #DataFrame de apoio
    dados2 = dados.copy()

    #passa a quantidade absoluta para a quantidade por dia
    for i in range(1, dados.shape[0]):
        dados['quantidade'][i] = dados2['quantidade'][i] - dados2['quantidade'][i-1]
    if(dados.shape[0]<7):
        print('falta fazer')
    else:
        for i in reversed(range(dados.shape[0]-24, dados.shape[0])):
            if(int(dados['hora'][i])==0):
                dia[0] = round(dados['quantidade'][i],2)
                break
            else:
                dia[int(dados['hora'][i])] = round(dados['quantidade'][i],2)

    #print(dia)

    #GRAFICO DO DIA
    dark_lighten_style = LightenStyle('#336676')
    day_graph=pygal.Bar(width=1000, style=dark_lighten_style)
    day_graph.title = "Consumo do dia"

    for i in range(24):
        day_graph.add(str(i), dia[i])

    #day_graph.render_in_browser()
    day_graph.render_to_file('static/day_graph.svg')
