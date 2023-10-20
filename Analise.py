import pandas as pd
import plotly_express as px
dados = pd.read_excel("vendas.xlsx")

eixoX = input("O que analisar no eixo X?: ")
eixoY = input("O que analisar no eixo Y?: ")
cor = input("O que analisar no eixo na cor?: ")

grafico = px.histogram(dados, x=eixoX,y=eixoY, color=cor, text_auto=True)
grafico.write_html("grafico.html")
