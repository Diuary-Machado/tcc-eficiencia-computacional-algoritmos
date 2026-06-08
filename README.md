# Eficiência Computacional e Escalabilidade em Algoritmos de Previsão
> :chart_with_upwards_trend: **Estudo Aplicado a Séries Temporais Financeiras (TCC)**

---

## :black_nib: Sobre o Projeto
Este projeto analisa e compara a eficiência computacional, o consumo de recursos de hardware (RAM/CPU) e a escalabilidade de diferentes algoritmos de Machine Learning e Deep Learning aplicados à previsão de séries temporais do mercado financeiro.

O foco principal está em entender o custo-benefício (*trade-off*) entre o tempo de processamento necessário por cada infraestrutura e a precisão das previsões em cenários de baixa/media/alta volumetria de dados.

---

## :bar_chart: Modelos Analisados
O ecossistema do projeto avalia duas abordagens distintas de modelagem:
* **Estatístico Clássico:** ARIMA
* **Machine Learning (Boosting):** XGBoost

---

## :hammer_and_wrench: Tecnologias e Bibliotecas
* **Linguagem Principal:** Python 3.10+
* **Manipulação de Dados:** `pandas`, `numpy`
* **Modelagem e ML:** `xgboost`, `scikit-learn`, `statsmodels`
* **Deep Learning:** `tensorflow` / `keras`
* **Visualização Dinâmica:** `plotly`

---

## :file_folder: Estrutura do Repositório
```tree
├── Graficos/             # Gráficos gerados
├── Graficos dinamicos/   # Gráficos interativos exportados em HTML
├── Resultados/           # BenchMarks e dados em CSV
├── Src/                  # Pasta Source (Código-fonte)
│   ├── gerador_de graficos.py
│   ├── gerador_de graficos_dinamicos.py
│   └── motor_benchmark.py
├── .Gitattributes        # Configurações de exibição do repositório
├── .Gitignore            # Arquivos ignorados pelo Git
├── .README.md            # Arquivos destinado a documentar o projeto
├──  Main.py              # Script principal para execução dos benchmarks
└──  Requirtements.txt    # Dependências do projeto para replicação       

