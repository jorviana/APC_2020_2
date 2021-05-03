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
import json
import pandas as pd
py.init_notebook_mode(connected=True)

#---------------------------------------------------------Função de nomear---------------------------------------------------------------------------------------
def name_to_sigla(name):                                                                #Renomeia as siglas para relacionar as do arquivo json com as do arquivo csv
    if name == "Norte":                                                                 #Se sigla igual à Norte
        return "N"                                                                      #Retorna N
    if name == "Nordeste":                                                              #Se sigla igual à Nordeste
        return "NE"                                                                     #Retorna NE
    if name == "Centro-Oeste":                                                          #Se sigla igual à Centro-Oeste
        return "CO"                                                                     #Retorna CO
    if name == "Sudeste":                                                               #Se sigla igual à Sudeste
        return "SE"                                                                     #Retorna SE
    if name == "Sul":                                                                   #Se sigla igual à Sul
        return "S"                                                                      #Retorna S
    
#-------------------------------------------------Leitura de json-----------------------------------------------------------------
f = open("brazil_reg.json")                                                            #Abre o arquivo GEOJSON dividindo o mapa por região
br = json.loads(f.read())                                                              #Lê arquivo json

#-------------------------------------------Dashboard-------------------------------------------------------------------------------------------------------------------------------
app = dash.Dash(__name__)                                                               #Criação da dash                          

app.layout = html.Div(children=[                                                        #Div realiza a divisão da pagina 
    html.H1(children= 'Panorama da Energia Elétrica no Brasil', style = {"text-align":"center"}),  
    html.Hr(),                                                                          #Divisão de 1 linha
    html.Div([                                                                          #Divisão da pagina     
        dcc.Dropdown(id='classe1',                                                      #Nome da ID dos gráficos
        options=[
            {'label': '2012', 'value': '2012'},                                         #Declaração de label - 2012
            {'label': '2013', 'value': '2013'},                                         #Declaração de label - 2013
            {'label': '2014', 'value': '2014'},                                         #Declaração de label - 2014
            {'label': '2015', 'value': '2015'},                                         #Declaração de label - 2015
            {'label': '2016', 'value': '2016'},                                         #Declaração de label - 2016
            {'label': '2017', 'value': '2017'},                                         #Declaração de label - 2017
            {'label': '2018', 'value': '2018'}                                          #Declaração de label - 2018
        ],
        value='2012'),                                                                  #Inicia pela label 2012
                                                 
        ],style={'color':'blue', 'width':'40%'}),                                       #Color é referente a cor da grade
        dcc.Graph(id='fig_ano_2012')                                                    #Width referente ao espaço que toma da tela
    
], style={'background':'#183446', 'color':'white'})                                     #Background é referente a cor de fundo, 
                                                                                        #Color é referente a cor das labels
    
@app.callback(                                                                          #Declaração de entradas e saída      
    Output('fig_ano_2012', 'figure'),                                                   #As saída são as figuras
    Input('classe1', 'value')                                                           #A entrada é referente a ID
)
#-------------------------------------------Gráfico-------------------------------------------------------------------------------------------------------------------------------
def luz_para_todos(year):
    f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.24.csv")
    lines = f.read().split("\n")                                                           # f.read lê todo o conteúdo do arquivo e retorna uma string
                                                                                           # .split("\n") divide essa string do conteudo em linhas
    siglas = []                                                                            #Lista vazia que armazena as siglas

    populations = []                                                                       #Lista vazia que armazena os dados de população                                                                         #Determinação dos anos

    for l in lines[10:-2]:                                                                 #Lê as linhas começando da linha 10 e excluindo as duas últimas linhas
        ls = l.split(",")                                                                  #.split(",") separa elementos por vírgula da lista
        siglas.append(name_to_sigla(ls[1]))                                                #Insere na lista siglas cada elemento de name_to_sigla que esteja na posição 1 da lista
        population_str = ls[int(year[-1])].strip()                                         #.strip retira todos os espaços do começo e do inicio da string então '   -    ' fica '-'
        if population_str == '-':                                                          #Compara a string recebida com o '-'
            population = 0                                                                 #Se True '-' é igual a 0
        else:
            population = float(population_str)                                             #Se False transforma a string recebida num float

        populations.append(population)                                                     #Insere na lista population cada elemento de population

  
    d = {"regiao": siglas, "populacao": populations}  

    fig = px.choropleth(d, geojson=br, locations='regiao', color='populacao',             #Grafico de heatmap, com geojson dividido por região do br
                                 color_continuous_scale="PuBu",                           #Cor definida
                                featureidkey="properties.SIGLA",                          #Chave de interesse 
                               range_color=(0, 200),                                      #A internsidade das cores, o range
                               scope="south america",                                     #Mapa da america do sul
                               labels={'populacao':'População (mil)'},                    #Label do gráfico
                          )
    fig.update_layout(
        title_text = 'Distribuição Regional do Programa Luz Para Todos no Ano de {} (por mil habitantes)'.format(year),   
    )
    return fig
                                                        

    
if __name__== '__main__':                                                               #Retorno da main
    app.run_server()                                                                    #Roda servidor

