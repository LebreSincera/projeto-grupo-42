import streamlit as st
import pandas as pd

st.set_page_config(page_title="BMW Sales Dashboard", layout="wide")

st.title('🚗 BMW Global Automotive Sales')

@st.cache_data
def load_data():
    # Agora que o arquivo está na pasta correta, a leitura é direta
    return pd.read_csv('bmw_global_sales_2018_2025.csv')

try:
    df = load_data()

    # --- MÉTRICAS NO TOPO ---
    total_vendas = df['Units_Sold'].sum()
    receita_total = df['Revenue_EUR'].sum()
    media_ev = df['BEV_Share'].mean() * 100

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Vendido", f"{total_vendas:,} un")
    m2.metric("Receita Total", f"€{receita_total:,.0f}")
    m3.metric("Participação Elétricos (Média)", f"{media_ev:.1f}%")

    st.divider()

    # --- GRÁFICOS ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Evolução de Vendas por Ano")
        vendas_ano = df.groupby('Year')['Units_Sold'].sum()
        st.line_chart(vendas_ano)

    with col2:
        st.subheader("📊 Vendas por Modelo")
        vendas_modelo = df.groupby('Model')['Units_Sold'].sum().sort_values(ascending=True)
        st.bar_chart(vendas_modelo)

    # --- TABELA DE DADOS ---
    with st.expander("Ver dados completos"):
        st.dataframe(df)

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")