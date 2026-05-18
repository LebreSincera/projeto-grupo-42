import streamlit as st
import pandas as pd
import plotly.express as px
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_DADOS = os.path.join(BASE_DIR, "Data", "base_tratada.csv")

PALETA_BMW = ["#000080", "#0066B1", "#3181FF", "#00AEEF", "#A9D6FF"]

st.set_page_config(
    page_title="BMW Sales Dashboard",
    layout="wide"
)

st.title("🚗 BMW Global Automotive Sales Dashboard")
st.caption("Criação de visualizações e gráficos estatísticos com Streamlit")

df = pd.read_csv(CAMINHO_DADOS)

# KPIs
total_vendas = df["Units_Sold"].sum()
total_modelos = df["Model"].nunique()
total_regioes = df["Region"].nunique()
ano_inicial = df["Year"].min()
ano_final = df["Year"].max()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Vendas", f"{total_vendas:,.0f}")
col2.metric("Modelos", total_modelos)
col3.metric("Regiões", total_regioes)
col4.metric("Período", f"{ano_inicial} - {ano_final}")

st.divider()

# Dados agrupados
vendas_regiao = df.groupby("Region")["Units_Sold"].sum().reset_index()

vendas_ano = df.groupby("Year")["Units_Sold"].sum().reset_index()

modelos = (
    df.groupby("Model")["Units_Sold"]
    .sum()
    .sort_values(ascending=True)
    .reset_index()
)

vendas_regiao_ano = (
    df.groupby(["Year", "Region"])["Units_Sold"]
    .sum()
    .reset_index()
)

# Layout em colunas
col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("🌍 Vendas por Região")

    fig1 = px.bar(
        vendas_regiao,
        x="Region",
        y="Units_Sold",
        color="Region",
        color_discrete_sequence=PALETA_BMW,
        title="Volume total de vendas por região",
        labels={
            "Region": "Região",
            "Units_Sold": "Unidades vendidas"
        }
    )

    st.plotly_chart(fig1, use_container_width=True)

with col_dir:
    st.subheader("📈 Evolução das Vendas")

    fig2 = px.line(
        vendas_ano,
        x="Year",
        y="Units_Sold",
        markers=True,
        title="Evolução das vendas ao longo dos anos",
        labels={
            "Year": "Ano",
            "Units_Sold": "Unidades vendidas"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

col_esq2, col_dir2 = st.columns(2)

with col_esq2:
    st.subheader("🏆 Modelos Mais Vendidos")

    fig3 = px.bar(
        modelos,
        x="Units_Sold",
        y="Model",
        orientation="h",
        color="Units_Sold",
        color_continuous_scale=PALETA_BMW,
        title="Ranking de modelos mais vendidos",
        labels={
            "Units_Sold": "Unidades vendidas",
            "Model": "Modelo"
        }
    )

    fig3.update_layout(coloraxis_showscale=False)

    st.plotly_chart(fig3, use_container_width=True)

with col_dir2:
    st.subheader("📊 Vendas por Região ao Longo dos Anos")

    fig4 = px.bar(
        vendas_regiao_ano,
        x="Year",
        y="Units_Sold",
        color="Region",
        barmode="group",
        color_discrete_sequence=PALETA_BMW,
        title="Comparativo anual por região",
        labels={
            "Year": "Ano",
            "Units_Sold": "Unidades vendidas",
            "Region": "Região"
        }
    )

    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# Gráficos extras se as colunas existirem
col_esq3, col_dir3 = st.columns(2)

with col_esq3:
    if "BEV_Share" in df.columns:
        st.subheader("🔋 Participação de Veículos Elétricos")

        bev = df.groupby("Year")["BEV_Share"].mean().reset_index()

        fig5 = px.line(
            bev,
            x="Year",
            y="BEV_Share",
            markers=True,
            title="Média de participação BEV ao longo dos anos",
            labels={
                "Year": "Ano",
                "BEV_Share": "Participação BEV"
            }
        )

        st.plotly_chart(fig5, use_container_width=True)

with col_dir3:
    if "Avg_Price_EUR" in df.columns:
        st.subheader("💰 Preço Médio por Ano")

        preco = df.groupby("Year")["Avg_Price_EUR"].mean().reset_index()

        fig6 = px.line(
            preco,
            x="Year",
            y="Avg_Price_EUR",
            markers=True,
            title="Evolução do preço médio",
            labels={
                "Year": "Ano",
                "Avg_Price_EUR": "Preço médio EUR"
            }
        )

        st.plotly_chart(fig6, use_container_width=True)

st.divider()

st.subheader("📋 Base de Dados")
st.dataframe(df, use_container_width=True)