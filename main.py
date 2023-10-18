import yfinance as yf
import talib
from plyer import notification

def obter_dados_acao(ticker, periodo='1y'):
    try:
        acao = yf.Ticker(ticker)
        dados = acao.history(period=period)
        return dados
    except Exception as e:
        print(f"Erro ao obter dados da ação {ticker}: {e}")
        return None

def analise_tecnica(dados):
    try:
        # Adicionando indicadores simples para este exemplo
        dados['MA20'] = talib.SMA(dados['Close'], timeperiod=20)
        dados['MA50'] = talib.SMA(dados['Close'], timeperiod=50)
        dados['RSI'] = talib.RSI(dados['Close'], timeperiod=14)

        # Adapte e adicione mais indicadores conforme necessário

        return dados
    except Exception as e:
        print(f"Erro ao realizar análise técnica: {e}")
        return None

def enviar_notificacao(mensagem):
    notification.notify(
        title='Análise Técnica',
        message=mensagem,
        app_icon=None,
        timeout=10,
    )

# Substitua 'AAPL' pelo ticker da ação desejada
ticker = 'AAPL'

dados_acao = obter_dados_acao(ticker)
if dados_acao is not None:
    dados_analisados = analise_tecnica(dados_acao)

    if dados_analisados is not None:
        # Exemplo de condição simples para notificação (cruzamento de médias)
        if dados_analisados['MA20'].iloc[-1] > dados_analisados['MA50'].iloc[-1]:
            mensagem = f"{ticker}: Sinal de compra (MA20 acima de MA50)!"
        else:
            mensagem = f"{ticker}: Sem sinal de compra neste momento."

        # Adapte as condições de notificação conforme necessário
        enviar_notificacao(mensagem)
