"""
ETL - Limpeza e Tratamento da Base de Dados
Projeto Integrador - Grupo 42

Descrição:
    Lê a base original de vendas da BMW (base_original.csv),
    realiza o tratamento e salva o resultado em base_tratada.csv.
"""

import pandas as pd
import os

# Caminhos dos arquivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_ORIGINAL = os.path.join(BASE_DIR, "data", "base_original.csv")
CAMINHO_TRATADA  = os.path.join(BASE_DIR, "data", "base_tratada.csv")


def carregar_dados(caminho: str) -> pd.DataFrame:
    """Carrega o CSV original."""
    print(f"[ETL] Carregando dados de: {caminho}")
    df = pd.read_csv(caminho)
    print(f"[ETL] Shape inicial: {df.shape}")
    return df


def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica todas as etapas de limpeza e transformação."""

    # 1. Remover duplicatas
    antes = len(df)
    df = df.drop_duplicates()
    print(f"[ETL] Duplicatas removidas: {antes - len(df)}")

    # 2. Remover linhas onde colunas essenciais são nulas
    colunas_essenciais = ["Year", "Model", "Units_Sold", "Revenue_EUR", "Region"]
    antes = len(df)
    df = df.dropna(subset=colunas_essenciais)
    print(f"[ETL] Linhas com valores nulos removidas: {antes - len(df)}")

    # 3. Padronizar nomes de colunas (sem espaços, lowercase)
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # 4. Garantir tipos corretos
    df["Year"]        = df["Year"].astype(int)
    df["Units_Sold"]  = pd.to_numeric(df["Units_Sold"], errors="coerce").fillna(0).astype(int)
    df["Revenue_EUR"] = pd.to_numeric(df["Revenue_EUR"], errors="coerce").fillna(0.0)

    # 5. Padronizar coluna BEV_Share (garantir que está entre 0 e 1)
    if "BEV_Share" in df.columns:
        df["BEV_Share"] = pd.to_numeric(df["BEV_Share"], errors="coerce").fillna(0.0)
        df["BEV_Share"] = df["BEV_Share"].clip(0, 1)

    # 6. Padronizar texto das colunas categóricas
    for col in ["Model", "Region"]:
        if col in df.columns:
            df[col] = df[col].str.strip().str.title()

    # 7. Remover linhas com Units_Sold <= 0 (registros inválidos)
    antes = len(df)
    df = df[df["Units_Sold"] > 0]
    print(f"[ETL] Linhas com vendas inválidas removidas: {antes - len(df)}")

    # 8. Resetar índice
    df = df.reset_index(drop=True)

    print(f"[ETL] Shape final após tratamento: {df.shape}")
    return df


def salvar_dados(df: pd.DataFrame, caminho: str) -> None:
    """Salva o DataFrame tratado em CSV."""
    df.to_csv(caminho, index=False)
    print(f"[ETL] Base tratada salva em: {caminho}")


def main():
    df_original = carregar_dados(CAMINHO_ORIGINAL)
    df_tratada  = tratar_dados(df_original)
    salvar_dados(df_tratada, CAMINHO_TRATADA)
    print("[ETL] Processo concluído com sucesso!")


if __name__ == "__main__":
    main()
