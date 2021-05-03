#!/usr/bin/env python
# coding: utf-8

# In[1]:


#---------------------------------------------Importando Bibliotecas-------------------------------------------------------------------------------------------------------------------------------
import xlrd
import dash_core_components as dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
import pandas as pd
import re
import dash_html_components as html
import plotly.express as px 
import plotly.offline as py 
import plotly.graph_objs as go
import pandas as pd 
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)


# In[2]:


#-------------------------------------------Região Norte----------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------Geração-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv", encoding="utf8") 
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Norte":                                                      #Condiciona que se o elemento 1 da lista for igual à "Norte" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float
        
     
linha = go.Scatter(x = years,                                                 #Linha é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   mode = 'lines',                                            #Modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]',                                    #Nome das linhas, no caso geração
                   line = {'color': '#38aecc'})                               #Cor das linhas

#---------------------------------------------Consumo-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv", encoding="utf8")
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Norte":                                                      #Condiciona que se o elemento 1 da lista for igual à "Norte" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float

barra = go.Bar(x = years,                                                     #Barra é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   name = 'Consumo [GWh]',                                    #Nome das barras, no caso consumo
                   marker = {'color': '#183446'})                             #Cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Norte [GWh]',        #Título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'},      #Título eixo y
                                xaxis={'title':''})                           #Título eixo x
trace = [linha, barra]                                                        #Trace é a variável que armazena gráficos
fig_norte = go.Figure(data=trace, layout=config)                              #Transforma em fig os gráficos com o layout determinado
fig_norte.show()                                                              #Plota os gráficos


# In[3]:


#-------------------------------------------Região Nordeste-------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------Geração-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv", encoding="utf8") 
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Nordeste":                                                   #Condiciona que se o elemento 1 da lista for igual à "Nordeste" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float
        
     
linha = go.Scatter(x = years,                                                 #Linha é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   mode = 'lines',                                            #Modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]',                                    #Nome das linhas, no caso geração
                   line = {'color': '#38aecc'})                               #Cor das linhas

#---------------------------------------------Consumo-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv", encoding="utf8")
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Nordeste":                                                   #Condiciona que se o elemento 1 da lista for igual à "Nordeste" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float

barra = go.Bar(x = years,                                                     #Barra é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   name = 'Consumo [GWh]',                                    #Nome das barras, no caso consumo
                   marker = {'color': '#183446'})                             #Cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Nordeste [GWh]',     #Título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'},      #Título eixo y
                                xaxis={'title':''})                           #Título eixo x
trace = [linha, barra]                                                        #Trace é a variável que armazena gráficos
fig_nordeste = go.Figure(data=trace, layout=config)                           #Transforma em fig os gráficos com o layout determinado
fig_nordeste.show()                                                           #Plota os gráficos


# In[4]:


#-------------------------------------------Região Centro-Oeste---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------Geração-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv", encoding="utf8") 
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Centro-Oeste":                                               #Condiciona que se o elemento 1 da lista for igual à "Centro-Oeste" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float
        
     
linha = go.Scatter(x = years,                                                 #Linha é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   mode = 'lines',                                            #Modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]',                                    #Nome das linhas, no caso geração
                   line = {'color': '#38aecc'})                               #Cor das linhas

#---------------------------------------------Consumo-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv", encoding="utf8")
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Centro-Oeste":                                               #Condiciona que se o elemento 1 da lista for igual à "Centro-Oeste" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float

barra = go.Bar(x = years,                                                     #Barra é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   name = 'Consumo [GWh]',                                    #Nome das barras, no caso consumo
                   marker = {'color': '#183446'})                             #Cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Centro-Oeste [GWh]', #Título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'},      #Título eixo y
                                xaxis={'title':''})                           #Título eixo x
trace = [linha, barra]                                                        #Trace é a variável que armazena gráficos
fig_centro_oeste = go.Figure(data=trace, layout=config)                       #Transforma em fig os gráficos com o layout determinado
fig_centro_oeste.show()                                                       #Plota os gráficos


# In[5]:


#-------------------------------------------Região Sudeste--------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------Geração-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv", encoding="utf8") 
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Sudeste":                                                    #Condiciona que se o elemento 1 da lista for igual à "Sudeste" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float
        
     
linha = go.Scatter(x = years,                                                 #Linha é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   mode = 'lines',                                            #Modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]',                                    #Nome das linhas, no caso geração
                   line = {'color': '#38aecc'})                               #Cor das linhas

#---------------------------------------------Consumo-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv", encoding="utf8")
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Sudeste":                                                    #Condiciona que se o elemento 1 da lista for igual à "Sudeste" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float

barra = go.Bar(x = years,                                                     #Barra é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   name = 'Consumo [GWh]',                                    #Nome das barras, no caso consumo
                   marker = {'color': '#183446'})                             #Cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Sudeste [GWh]',      #Título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'},      #Título eixo y
                                xaxis={'title':''}) #título eixo x
trace = [linha, barra]                                                        #Trace é a variável que armazena gráficos
fig_sudeste = go.Figure(data=trace, layout=config)                            #Transforma em fig os gráficos com o layout determinado
fig_sudeste.show()                                                            #Plota os gráficos


# In[6]:


#-------------------------------------------Região Sul------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------Geração-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv", encoding="utf8") 
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Sul":                                                        #Condiciona que se o elemento 1 da lista for igual à "Sul" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float
        
     
linha = go.Scatter(x = years,                                                 #Linha é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   mode = 'lines',                                            #Modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]',                                    #Nome das linhas, no caso geração
                   line = {'color': '#38aecc'})                                   #Cor das linhas

#---------------------------------------------Consumo-------------------------------------------------------------------------------------------------------------------------------
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv", encoding="utf8")
content = f.read().split("\n")                                                # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                              # .split("\n") divide essa string do conteudo em linhas
    
years = []                                                                    #Lista vazia que armazena os anos

for y in content[8].split(",")[2:-4]:                                         #for lê a oitava linha que contem os anos dentro do arquivo csv
                                                                              #.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
    
    years.append (int(y))                                                     #Insere na lista years cada elemento de y transformado de string para inteiro

data = []                                                                     #Lista vazia que armazena energia de cada região

for l in content:                                                             #for lê todas as linhas da lista

    ls = l.split(",")                                                         #.split(",") separa por vírgula

    if ls[1] == "Sul":                                                        #Condiciona que se o elemento 1 da lista for igual à "Sul" prossigo
        
        dt = ls[2:-5]                                                         #Determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        
        for l in dt:                                                          #Lê cada elemento da lista filtrada
            
            data.append(float(l))                                             #Insere na lista data cada elemento l transformado de string para float

barra = go.Bar(x = years,                                                     #Barra é a variável que armazena informações do gráfico, x é referente aos anos
                   y = data,                                                  #Energia do gráfico, eixo y
                   name = 'Consumo [GWh]',                                    #Nome das barras, no caso consumo
                   marker = {'color': '#183446'})                             #Cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Sul [GWh]',          #Título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'},      #Título eixo y
                                xaxis={'title':''})                           #Título eixo x
trace = [linha, barra]                                                        #Trace é a variável que armazena gráficos
fig_sul = go.Figure(data=trace, layout=config)                                #Transforma em fig os gráficos com o layout determinado
fig_sul.show()                                                                #Plota os gráficos


# In[ ]:


#-------------------------------------------Dashboard-------------------------------------------------------------------------------------------------------------------------------
app = dash.Dash(__name__)                                                      #Criação da dash                          

app.layout = html.Div(children=[                                               #Div realiza a divisão da pagina 
    html.H1(children= 'Panorama da Energia Elétrica no Brasil', style = {"text-align":"center"}),  
    html.Hr(),                                                                 #Divisão de 1 linha
    html.Div([                                                                 #Divisão da pagina     
        dcc.Dropdown(id='classe1',                                             #Nome da ID dos gráficos
        options=[
            {'label': 'Norte', 'value': 'Norte'},                              #Declaração de label - Norte
            {'label': 'Nordeste', 'value': 'Nordeste'},                        #Declaração de label - Nordeste
            {'label': 'Centro-Oeste', 'value': 'Centro'},                      #Declaração de label -  Centro-Oeste
            {'label': 'Sudeste', 'value': 'Sudeste'},                          #Declaração de label - Sudeste
            {'label': 'Sul', 'value': 'Sul'}                                   #Declaração de label - Sul
        ],
        value='Norte'),                                                        #Inicia pela label Norte
                                                 
        ],style={'color':'blue', 'width':'40%'}),                             #Color é referente a cor da grade
                                                                              #Width referente ao espaço que toma da tela
        dcc.Graph(id='fig_norte')                                             #Determina o gráfico inicial, no caso, Norte
        
    
], style={'background':'#183446', 'color':'white'})                           #Background é referente a cor de fundo, 
                                                                              #Color é referente a cor das labels
    
@app.callback(                                                                #Declaração de entradas e saída      
    Output('fig_norte', 'figure'),                                            #As saída são as figuras
    Input('classe1', 'value')                                                 #A entrada é referente a ID
) 
def geracao_consumo(local):                                                   #Função para gerar gráficos
    if local=='Norte':                                                        #Se label for norte
        return fig_norte                                                      #Retorna figura do gráfico do norte
    if local=='Nordeste':                                                     #Se label for nordeste
        return fig_nordeste                                                   #Retorna figura do gráfico do nordeste
    if local=='Centro':                                                       #Se label for centro
        return fig_centro_oeste                                               #Retorna figura do gráfico do centro-oeste
    if local=='Sudeste':                                                      #Se label for sudeste   
        return fig_sudeste                                                    #Retorna figura do gráfico do sudeste
    if local=='Sul':                                                          #Se label for sul
        return fig_sul                                                        #Retorna figura do gráfico do sul
    
if __name__== '__main__':                                                     #Retorno da main
    app.run_server()                                                          #Roda servidor


# In[ ]:




