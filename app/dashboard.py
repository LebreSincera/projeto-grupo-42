"""
Dashboard - Interface Interativa de Vendas BMW
Projeto Integrador - Grupo 42

Execução:
    Na raiz do projeto, rode:
    streamlit run projeto-grupo-42/app/dashboard.py
"""

import streamlit as st
import pandas as pd
import os

# Caminho para a base tratada
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_DADOS = os.path.join(BASE_DIR, "data", "base_tratada.csv")

st.set_page_config(page_title="BMW Sales Dashboard", layout="wide")

st.title("🚗 BMW Global Automotive Sales")
st.caption("Fonte: Base de dados de vendas globais BMW (2018–2025)")

@st.cache_data
def load_data():
    return pd.read_csv(CAMINHO_DADOS)

try:
    df = load_data()

    # ── FILTROS LATERAIS ──────────────────────────────────────────────────────
    st.sidebar.header("Filtros")

    anos = sorted(df["Year"].unique())
    ano_sel = st.sidebar.multiselect("Ano", anos, default=anos)

    regioes = sorted(df["Region"].unique())
    regiao_sel = st.sidebar.multiselect("Região", regioes, default=regioes)

    modelos = sorted(df["Model"].unique())
    modelo_sel = st.sidebar.multiselect("Modelo", modelos, default=modelos)

    df_filtrado = df[
        df["Year"].isin(ano_sel) &
        df["Region"].isin(regiao_sel) &
        df["Model"].isin(modelo_sel)
    ]

    # ── MÉTRICAS NO TOPO ──────────────────────────────────────────────────────
    total_vendas  = df_filtrado["Units_Sold"].sum()
    receita_total = df_filtrado["Revenue_EUR"].sum()
    media_ev      = df_filtrado["BEV_Share"].mean() * 100 if "BEV_Share" in df_filtrado.columns else 0

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Vendido",                  f"{total_vendas:,} un")
    m2.metric("Receita Total",                  f"€{receita_total:,.0f}")
    m3.metric("Participação Elétricos (Média)", f"{media_ev:.1f}%")

    st.divider()

    # ── OBJETIVO 1: Volume de vendas por região ───────────────────────────────
    st.subheader("🌍 Objetivo 1 — Volume de Vendas por Região")
    vendas_regiao = (
        df_filtrado.groupby("Region")["Units_Sold"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(vendas_regiao)

    st.divider()

    # ── OBJETIVO 2: Modelos mais comercializados ──────────────────────────────
    st.subheader("🏆 Objetivo 2 — Modelos Mais Comercializados")
    vendas_modelo = (
        df_filtrado.groupby("Model")["Units_Sold"]
        .sum()
        .sort_values(ascending=True)
    )
    st.bar_chart(vendas_modelo)

    st.divider()

    # ── OBJETIVO 3: Crescimento de vendas por região ──────────────────────────
    st.subheader("📈 Objetivo 3 — Crescimento de Vendas por Região ao Longo dos Anos")
    crescimento = (
        df_filtrado.groupby(["Year", "Region"])["Units_Sold"]
        .sum()
        .unstack(fill_value=0)
    )
    st.line_chart(crescimento)

    st.divider()

    # ── TABELA COMPLETA ───────────────────────────────────────────────────────
    with st.expander("📄 Ver dados completos"):
        st.dataframe(df_filtrado, width='stretch')

except FileNotFoundError:
    st.error(
        "⚠️ Base de dados não encontrada. "
        "Execute primeiro o script de ETL:\n\n"
        "```bash\npython src/etl.py\n```"
    )
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
