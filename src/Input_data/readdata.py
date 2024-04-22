import pandas as pd

from src.Input_data import Training_data

def bolsa(file):
    """
    Função para retornar uma lista de ativos da bolsa com base em um csv existente
    """
    df = pd.read_csv(file)
    return df["Ticker"].tolist()

#training_data = Training_data(Training_data.bolsa("./acoes-listadas-b3.csv"), '2015-01-01', '2019-12-31')
training_data = Training_data(["KLBN11"], '2018-01-01', '2019-12-31')
print(training_data.p_pv())
