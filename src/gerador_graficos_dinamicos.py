import pandas as pd
import plotly.graph_objects as go
import os

def carregar_dados(ticker):
    nome_minulo = ticker.replace('.SA', '').lower()
    nome_maiusculo = ticker.replace('.SA', '').upper()
    
    caminho_csv = os.path.join("resultados", f"benchmark_{nome_minulo}.csv")
    if not os.path.exists(caminho_csv):
        caminho_csv = os.path.join("resultados", f"benchmark_{nome_maiusculo}.csv")
        
    if not os.path.exists(caminho_csv):
        print(f"Arquivo não encontrado para {ticker}.")
        return None, nome_minulo

    try:
        df = pd.read_csv(caminho_csv, sep=';', decimal=',')
    except:
        df = pd.read_csv(caminho_csv, sep=',', decimal='.')
        
    return df, nome_minulo

def gerar_grafico_tempo(df, nome_minulo, ticker):
    df_arima = df[df['Algoritmo'] == 'ARIMA']
    df_xgb = df[df['Algoritmo'] == 'XGBoost']

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_arima['Cenario'], y=df_arima['Tempo_s'],
        mode='lines+markers', name='ARIMA (Estatístico)',
        line=dict(color='#e63946', width=4), marker=dict(size=10)
    ))

    fig.add_trace(go.Scatter(
        x=df_xgb['Cenario'], y=df_xgb['Tempo_s'],
        mode='lines+markers', name='XGBoost (Machine Learning)',
        line=dict(color='#2a9d8f', width=4), marker=dict(size=10)
    ))

    fig.update_layout(
        title=dict(text=f'<b>Escalabilidade Temporal - {ticker}</b>', font=dict(size=20)),
        xaxis_title='<b>Volume de Dados (Cenários)</b>',
        yaxis_title='<b>Tempo em Segundos</b>',
        hovermode='x unified',
        plot_bgcolor='white',
        updatemenus=[
            dict(
                type="buttons", direction="right",
                x=0.5, y=1.15, xanchor='center', yanchor='top',
                showactive=True,
                buttons=list([
                    dict(args=[{"yaxis.type": "linear"}], label="Escala Linear", method="relayout"),
                    dict(args=[{"yaxis.type": "log"}], label="Escala Logarítmica", method="relayout")
                ]),
                bgcolor="#f8f9fa", bordercolor="#ced4da"
            )
        ]
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

    caminho_html = os.path.join("graficos dinamicos", f"interativo_tempo_{nome_minulo}.html")
    fig.write_html(caminho_html)
    print(f"Gerado: {caminho_html}")

def gerar_grafico_ram(df, nome_minulo, ticker):
    df_arima = df[df['Algoritmo'] == 'ARIMA']
    df_xgb = df[df['Algoritmo'] == 'XGBoost']

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_arima['Cenario'], y=df_arima['RAM_MB'],
        name='ARIMA (Estatístico)', marker_color='#e63946'
    ))

    fig.add_trace(go.Bar(
        x=df_xgb['Cenario'], y=df_xgb['RAM_MB'],
        name='XGBoost (Machine Learning)', marker_color='#2a9d8f'
    ))

    fig.update_layout(
        title=dict(text=f'<b>Eficiência Espacial (Pico de RAM) - {ticker}</b>', font=dict(size=20)),
        xaxis_title='<b>Volume de Dados (Cenários)</b>',
        yaxis_title='<b>Memória RAM Consumida (MB)</b>',
        barmode='group',
        hovermode='x unified',
        plot_bgcolor='white',
        updatemenus=[
            dict(
                type="buttons", direction="right",
                x=0.5, y=1.15, xanchor='center', yanchor='top',
                showactive=True,
                buttons=list([
                    dict(args=[{"yaxis.type": "linear"}], label="Escala Linear", method="relayout"),
                    dict(args=[{"yaxis.type": "log"}], label="Escala Logarítmica", method="relayout")
                ]),
                bgcolor="#f8f9fa", bordercolor="#ced4da"
            )
        ]
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

    caminho_html = os.path.join("graficos dinamicos", f"interativo_ram_{nome_minulo}.html")
    fig.write_html(caminho_html)
    print(f"Gerado: {caminho_html}")

if __name__ == "__main__":
    pasta_destino = "graficos dinamicos"
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    print("Iniciando geração de Dashboards Interativos...")
    datasets = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]
    
    for ativo in datasets:
        df, nome_minulo = carregar_dados(ativo)
        if df is not None:
            gerar_grafico_tempo(df, nome_minulo, ativo)
            gerar_grafico_ram(df, nome_minulo, ativo)
            
    print(f"Todos os gráficos interativos foram gerados na pasta '{pasta_destino}'!")