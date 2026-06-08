# Eficiência Computacional e Escalabilidade em Algoritmos de Previsão
> :chart_with_upwards_trend: **Estudo Aplicado a Séries Temporais Financeiras (TCC)**

---

## :black_nib: Sobre o Projeto
Este projeto analisa e compara a eficiência computacional, o consumo de recursos de hardware (RAM/CPU) e a escalabilidade de diferentes algoritmos de Machine Learning e Deep Learning aplicados à previsão de séries temporais do mercado financeiro.

O foco principal está em entender o custo-benefício (*trade-off*) entre o tempo de processamento necessário por cada infraestrutura e a precisão das previsões em cenários de baixa/media/alta volumetria de dados.

---

## :bar_chart: Modelos Analisados
O ecossistema do projeto avalia duas abordagens distintas de modelagem:
* **AutoRegressive Integrated Moving Average:** ARIMA
* **eXtreme Gradient Boosting:** XGBoost

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
│   ├── gerador_de_graficos.py
│   ├── gerador_de_graficos_dinamicos.py
│   └── motor_benchmark.py
├── .Gitattributes        # Configurações de exibição do repositório
├── .Gitignore            # Arquivos ignorados pelo Git
├── .README.md            # Arquivos destinado a documentar o projeto
├──  Main.py              # Script principal para execução dos benchmarks
└──  Requirtements.txt    # Dependências do projeto para replicação       
```

---

## :computer: Como Executar o Projeto

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/Diuary-Machado/tcc-eficiencia-computacional-algoritmos.git
cd tcc-Eficincia-computacional-algoritimos
```

---

### 2️⃣ Criar o Ambiente Virtual

```bash
python -m venv venv
```

#### Windows (PowerShell)

```bash
.\venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 3️⃣ Instalar as Dependências

```bash
pip install -r requirements.txt
```

---

## :rocket: Executando a Aplicação

### Passo A — Executar os Benchmarks

Executa os algoritmos de previsão e registra o consumo de hardware.

```bash
python Main.py
```

Os resultados serão armazenados em:

```text
Resultados/
```

---

### Passo B — Gerar Gráficos Estáticos

Cria gráficos comparativos em formato de imagem.

```bash
python Src/gerador_de_graficos.py
```

Arquivos gerados em:

```text
Graficos/
```

---

### Passo C — Gerar Gráficos Dinâmicos

Gera dashboards interativos em HTML.

```bash
python Src/gerador_de_graficos_dinamicos.py
```

Arquivos gerados em:

```text
Graficos dinamicos/
```

---

## :chart_with_upwards_trend: Resultados Gerados

Após a execução completa serão produzidos:

### :page_facing_up: Relatórios e Métricas

```text
Resultados/
```

Contendo:

* Tempo de execução
* Consumo de CPU
* Consumo de memória RAM
* Métricas de previsão
* Benchmarks computacionais

### :bar_chart: Gráficos Estáticos

```text
Graficos/
```

Contendo imagens prontas para:

* Artigos científicos
* Apresentações
* Relatórios técnicos

### :globe_with_meridians: Visualizações Interativas

```text
Graficos dinamicos/
```

Contendo gráficos HTML navegáveis e interativos.

---

## :mortar_board: Trabalho de Conclusão de Curso

**Autor:** Diuary Machado

**Curso:** Engenharia de Software

**Tema do TCC:**

> Eficiência Computacional e Escalabilidade em Algoritmos de Previsão Aplicados a Séries Temporais Financeiras

---

## :memo: Licença

Este projeto foi desenvolvido exclusivamente para fins acadêmicos e de pesquisa.