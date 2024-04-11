import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def cotacao(bolsa:list, data_inicial:str, data_final:str):
    """
    Função para retornar o grafico de cotações de uma lista de ativos
    para data inicial e final informados pelo usuário tem que estar seguindo o formato yyyy-mm-dd
    """
    for acao in bolsa:
        df = yf.download(acao+'.SA', start=data_inicial, end=data_final)
        df = df["Adj Close"].plot(figsize=(10, 5))
    return plt.show()

def bolsa(file):
    """
    Função para retornar uma lista de ativos da bolsa com base em um csv existente
    """
    df = pd.read_csv(file)
    return df["Ticker"].tolist()

print(cotacao(bolsa("acoes-listadas-b3.csv"), '2020-01-01', '2020-12-31'))

