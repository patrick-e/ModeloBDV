
import pandas as pd


from Input_data.classrequest import Training_data
from Input_data.readdata import bolsa

def Xdesempenho(start_value, end_value):
    """
    Função para retornar o desempenho da ação em booleana
    """
    desempenho = (start_value - end_value) / start_value
    if desempenho > 0.1:  
        return 1
    return 0

def Xp_pv(value):
    """
    Função para retornar o p/vp da ação em booleana
    """
    if value >= 1:
        return 1
    return 0

def Xdividend_yield(value):
    """
    Função para retornar o dividend yield da ação em booleana
    """
    if value >= 0.02:
        return  1
    return 0


# Obtendo os dados de cotação das ações
#data = Training_data(bolsa("./Input_data/acoes-listadas-b3.csv")[:10:], '2019-01-01', '2020-01-01')
data = Training_data(['ITUB4',"BBDC4"], '2019-01-01', '2020-01-01')
values = pd.DataFrame(data.cotacao())


for ppv in data.p_pv().items():
    Xp_pv(ppv[1])



for ticker in values.columns:
    valuestart = values[ticker].iloc[0]  # Valor de início do período
    valueend = values[ticker].iloc[-1]   # Valor do fim do período

    # Calculando o desempenho da ação
    performance = Xdesempenho(valuestart, valueend)
    
    print("Desempenho:", performance)
