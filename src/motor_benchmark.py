import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import tracemalloc
import os
import warnings
from statsmodels.tsa.arima.model import ARIMA
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

warnings.filterwarnings("ignore")

def gerar_dados_escala(serie_base, tamanho_alvo):
    valores_1d = serie_base.values.flatten()
    repeticoes = (tamanho_alvo // len(valores_1d)) + 1
    dados_expandidos = np.tile(valores_1d, repeticoes)[:tamanho_alvo]
    ruido = np.random.normal(0, 0.5, tamanho_alvo)
    return pd.Series(dados_expandidos + ruido)

def preparar_dados_xgb(serie):
    df = pd.DataFrame(serie.values, columns=['Preco'])
    for i in range(1, 6):
        df[f'Lag_{i}'] = df['Preco'].shift(i)
    return df.dropna()

def executar_pipeline_completo(ticker, data_inicio="2020-01-01", data_fim="2025-01-01"):
    nome_base = ticker.replace('.SA', '').lower()
    
    print(f"\n--- Processando Base de Dados: {ticker} ---")
    
    # 1. Download
    dados = yf.download(ticker, start=data_inicio, end=data_fim, progress=False)
    dados_reais = dados['Close'].squeeze().dropna()
    
    # 2. Gráfico Histórico
    plt.figure(figsize=(10, 5))
    plt.plot(dados_reais.index, dados_reais.values, label=f'{ticker} - Fechamento')
    plt.title(f'Histórico {ticker}')
    plt.grid(True, linestyle='--', alpha=0.7)
    caminho_grafico = os.path.join("graficos", f"historico_{nome_base}.png")
    plt.savefig(caminho_grafico)
    plt.close()

    # 3. Preparação Carga/Escala
    cenarios = {
        "1_Leve(~1.200)": dados_reais,
        "2_Media(5.000)": gerar_dados_escala(dados_reais, 5000),
        "3_Alta(10.000)": gerar_dados_escala(dados_reais, 10000)
    }

    resultados = []

    # 4. Loop de Benchmark
    for nome_cenario, dados_cenario in cenarios.items():
        treino_a, teste_a = dados_cenario.iloc[:int(len(dados_cenario)*0.8)], dados_cenario.iloc[int(len(dados_cenario)*0.8):]
        
        # ARIMA
        tracemalloc.start() 
        t0 = time.time()
        ARIMA(treino_a, order=(5, 1, 0)).fit().forecast(steps=len(teste_a))
        tempo_arima = time.time() - t0
        _, pico_arima = tracemalloc.get_traced_memory() 
        tracemalloc.stop()
        
        # XGBoost
        df_x = preparar_dados_xgb(dados_cenario)
        X, y = df_x.drop('Preco', axis=1), df_x['Preco']
        X_tr, X_te = X.iloc[:int(len(df_x)*0.8)], X.iloc[int(len(df_x)*0.8):]
        y_tr = y.iloc[:int(len(df_x)*0.8)]
        
        modelo_xgb = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
        tracemalloc.start() 
        t0 = time.time()
        modelo_xgb.fit(X_tr, y_tr)
        modelo_xgb.predict(X_te)
        tempo_xgb = time.time() - t0
        _, pico_xgb = tracemalloc.get_traced_memory() 
        tracemalloc.stop()

        resultados.extend([
            {"Ativo": ticker, "Cenario": nome_cenario, "Algoritmo": "ARIMA", "Tempo_s": tempo_arima, "RAM_MB": pico_arima / 1024**2},
            {"Ativo": ticker, "Cenario": nome_cenario, "Algoritmo": "XGBoost", "Tempo_s": tempo_xgb, "RAM_MB": pico_xgb / 1024**2}
        ])

    # 5. Exportação
    caminho_csv = os.path.join("resultados", f"benchmark_{nome_base}.csv")
    pd.DataFrame(resultados).to_csv(caminho_csv, index=False, sep=';', decimal=',')
    print(f"[{ticker}] Concluído! Arquivos gerados em /resultados e /graficos.")