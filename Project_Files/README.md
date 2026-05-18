# projeto-grupo-42

## Equipe
- THIAGO JULIANI DE OLIVEIRA
- MATHEUS SANTOS SAMPAIO
- LUCAS BARROS DE ALMEIDA
- PEDRO OLIVEIRA SOUZA
- EWERTON DOS SANTOS GONCALVES
- RAFAEL SILVA COELHO

---

## Objetivo
- Realizar a análise da base de dados de vendas da BMW.
- Os objetivos específicos da análise são:
  1. Examinar o volume de vendas por região (Europa, China, EUA e demais mercados);
  2. Identificar os modelos mais comercializados;
  3. Comparar o crescimento das vendas entre diferentes regiões.

## Finalidade da análise
- Compreender de forma mais aprofundada o mercado de vendas da BMW e sua distribuição global.

---

## Estrutura do Repositório

```
projeto-grupo-42/
├── data/
│   ├── base_original.csv     # Base de dados bruta (adicionar manualmente)
│   └── base_tratada.csv      # Gerada automaticamente pelo ETL
├── src/
│   └── etl.py                # Limpeza e tratamento dos dados
├── app/
│   └── dashboard.py          # Interface interativa em Streamlit
├── requirements.txt          # Dependências do projeto
└── README.md
```

---

## Como executar

> **Pré-requisito:** ter o [Python](https://www.python.org/downloads/) instalado na máquina.

### Windows
Dê dois cliques no arquivo **`rodar_dashboard.bat`** na raiz do projeto.

### Linux / Mac
No terminal, na raiz do projeto, rode:
```bash
chmod +x rodar_dashboard.sh
./rodar_dashboard.sh
```

O script irá automaticamente:
1. Criar o ambiente virtual (`.venv`)
2. Instalar todas as dependências
3. Abrir o dashboard no navegador

---

## Executando manualmente (opcional)

Caso prefira rodar passo a passo:

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

# 2. Instalar dependências
pip install -r projeto-grupo-42/requirements.txt

# 3. Gerar a base tratada
python projeto-grupo-42/src/etl.py

# 4. Rodar o dashboard
streamlit run projeto-grupo-42/app/dashboard.py
```

---

## Planejamento
- **Tarefa 1:** Limpeza e tratamento da base de dados (CSV) — LUCAS BARROS DE ALMEIDA
- **Tarefa 2:** Desenvolvimento da lógica de filtros e consultas — PEDRO OLIVEIRA SOUZA
- **Tarefa 3:** Criação de visualizações e gráficos estatísticos — EWERTON DOS SANTOS GONCALVES
- **Tarefa 4:** Construção da interface interativa em Streamlit — THIAGO JULIANI DE OLIVEIRA
- **Tarefa 5:** Documentação técnica e revisão final — MATHEUS SANTOS SAMPAIO

---

## Tecnologias
- Python
- Pandas
- Plotly
- Streamlit
