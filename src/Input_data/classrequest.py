import yfinance as yf
import matplotlib.pyplot as plt
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
        for acao in self.ticker:
            df = yf.download(acao+'.SA', start=self.data_inicial, end=self.data_final)
            df = df["Adj Close"].plot(figsize=(10, 5))
        return plt.show()
    
    def dividendoyield(self):
        """
        Função para retornar o grafico de dividendos
        """
        dividendos = {}
        for acao in self.ticker:
            acao_data = yf.Ticker(acao+'.SA')
            df_dividends = acao_data.dividends
            df_dividends = df_dividends[df_dividends.index >= self.data_inicial]
            df_dividends = df_dividends[df_dividends.index <= self.data_final]
            dividendos[acao] = df_dividends
            print(f"ação vista:  {acao}" )
        return dividendos
    def p_pv(self):
        p_vp_dict = {}
        for acao in self.ticker:
            empresa = yf.Ticker(acao+'.SA')
            dados = empresa.balance_sheet
            dados = dados.transpose()

            patrimonio_liquido = dados['Stockholders Equity']  # Patrimônio líquido
            acoes_em_circulacao = empresa.info['sharesOutstanding']

            vp_por_acao = patrimonio_liquido / acoes_em_circulacao
            preco_atual = empresa.history(period='1d')['Close'][0]

            p_vp = preco_atual / vp_por_acao
            p_vp_dict[acao] = p_vp
        return p_vp_dict




