import yfinance as yf
from datetime import datetime

import pandas as pd


class Training_data:
    def __init__(self, ticker:list,data_inicial:str, data_final:str):
        """ 
        O ticker é a cota da bolsa,para data inicial e final informados
        pelo usuário tem que estar seguindo o formato yyyy-mm-dd
        """
        self.ticker = ticker
        self.data_inicial = data_inicial
        self.data_final = data_final
    def cotacao(self):
        """
        Função para retornar o grafico de cotações de uma lista de ativos
        """
        cotacao = {}
        for acao in self.ticker:
            df = yf.download(acao+'.SA', start=self.data_inicial, end=self.data_final)
            df = df["Adj Close"]
            cotacao[acao] = df
        return {acao:df for acao,df in cotacao.items()}
    
    def dividendoyield(self):
        """
        Função para retornar dividendos e dividend yield
        """
        dividendos = {}
        for acao in self.ticker:
            acao_data = yf.Ticker(acao+'.SA')
            df_dividends = acao_data.dividends
            df_dividends = df_dividends[df_dividends.index >= self.data_inicial]
            df_dividends = df_dividends[df_dividends.index <= self.data_final]
            
            # Cálculo do dividend yield
            preco_atual = acao_data.history(period='1d')['Close'].iloc[-1]
            dividend_yield = (df_dividends.sum() / preco_atual) * 100
            
            dividendos[acao] = {'Dividendos': df_dividends, 'DividendYield': dividend_yield}
        return dividendos
    def calcular_dias(self):
        # Converter as datas para o formato datetime
        data_inicial = datetime.strptime(self.data_inicial, '%Y-%m-%d')
        data_final = datetime.strptime(self.data_final, '%Y-%m-%d')
        # Calcular a diferença em dias
        dias = (data_final - data_inicial).days
        return dias
    def p_pv(self):
        p_vp_dict = {}
        dias = self.calcular_dias()
        for acao in self.ticker:
            empresa = yf.Ticker(acao+'.SA')
            dados = empresa.balance_sheet
            dados = dados.transpose()

            patrimonio_liquido = dados['Stockholders Equity']  # Patrimônio líquido
            acoes_em_circulacao = empresa.info['sharesOutstanding']

            vp_por_acao = patrimonio_liquido / acoes_em_circulacao
            periodo = f'{dias}d'
            preco_atual = (empresa.history(period=periodo)['Close'].iloc[-1])

            p_vp = preco_atual / vp_por_acao
            p_vp_dict[acao] = p_vp
        return {acao: p_vp_dict[acao].iloc[-1] for acao in p_vp_dict}




