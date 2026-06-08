import pandas as pd
import matplotlib.pyplot as plt
import os

def gerar_graficos_finais(ticker):
    nome_base = ticker.replace('.SA', '').lower()
    caminho_csv = os.path.join("resultados", f"benchmark_{nome_base}.csv")
    
    if not os.path.exists(caminho_csv):
        print(f"Arquivo não encontrado: {caminho_csv}")
        return

    df = pd.read_csv(caminho_csv, sep=';', decimal=',')

    # GRÁFICO 1: TEMPO DE EXECUÇÃO VS CARGA
    plt.figure(figsize=(10, 6))
    df_arima = df[df['Algoritmo'] == 'ARIMA']
    df_xgb = df[df['Algoritmo'] == 'XGBoost']

    plt.plot(df_arima['Cenario'], df_arima['Tempo_s'], marker='o', linewidth=2, label='ARIMA (Estatístico)', color='red')
    plt.plot(df_xgb['Cenario'], df_xgb['Tempo_s'], marker='s', linewidth=2, label='XGBoost (Machine Learning)', color='green')

    plt.title(f'Escalabilidade: Tempo de Execução - {ticker}', fontsize=14, fontweight='bold')
    plt.xlabel('Volume de Dados (Cenários)', fontsize=12)
    plt.ylabel('Tempo Total em Segundos', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)

    caminho_grafico_tempo = os.path.join("graficos", f"grafico_tempo_{nome_base}.png")
    plt.savefig(caminho_grafico_tempo)
    plt.close()

    # GRÁFICO 2: CONSUMO DE MEMÓRIA RAM (PICO)
    plt.figure(figsize=(10, 6))
    largura_barra = 0.35
    indices = range(len(df_arima['Cenario']))

    barras_arima = plt.bar([i - largura_barra/2 for i in indices], df_arima['RAM_MB'], largura_barra, label='ARIMA', color='salmon')
    barras_xgb = plt.bar([i + largura_barra/2 for i in indices], df_xgb['RAM_MB'], largura_barra, label='XGBoost', color='lightgreen')

    for barra in barras_arima:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura + 0.5, f'{altura:.1f} MB', ha='center', va='bottom', fontsize=9)
        
    for barra in barras_xgb:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura + 0.5, f'{altura:.2f} MB', ha='center', va='bottom', fontsize=9)

    plt.title(f'Eficiência: Pico de Memória RAM - {ticker}', fontsize=14, fontweight='bold')
    plt.xlabel('Volume de Dados (Cenários)', fontsize=12)
    plt.ylabel('Memória RAM Consumida (MB)', fontsize=12)
    plt.xticks(indices, df_arima['Cenario'])
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.ylim(0, max(df_arima['RAM_MB'].max(), df_xgb['RAM_MB'].max()) + 5)

    caminho_grafico_ram = os.path.join("graficos", f"grafico_ram_{nome_base}.png")
    plt.savefig(caminho_grafico_ram)
    plt.close()

    print(f"Gráficos científicos gerados para {ticker} na pasta 'graficos'!")

if __name__ == "__main__":
    print("Iniciando geração de gráficos em lote...")
    datasets_para_testar = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]
    
    for ativo in datasets_para_testar:
        gerar_graficos_finais(ativo)
        
    print("Processo finalizado!")