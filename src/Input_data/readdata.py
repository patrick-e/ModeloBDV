import pandas as pd


def bolsa(file) -> list:
    """
    Função para retornar uma lista de ativos da bolsa com base em um csv existente
    """
    df = pd.read_csv(file)
    return df["Ticker"].tolist()

